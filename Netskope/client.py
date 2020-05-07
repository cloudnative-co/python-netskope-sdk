import json
import re
import urllib.request
import urllib.parse
from .Exception import APIException
from .Utils import get_arguments
import http


class Client(object):
    headers: dict = dict()
    host: str = "https://{tenant}.goskope.com/api/{version}/"
    token: str = None

    def __init__(
        self, tenant: str = None, version: str = "v1", token: str = None,
        client: object = None
    ):
        if client is not None:
            self.host = client.host
            self.headers = client.headers
            self.token = client.token
        else:
            self.headers = {'content-type': "application/json"}
            args = get_arguments(locals(), keys=["tenant", "version"])
            self.host = self.host.format(**args)
            self.token = token

    def request(
        self,
        method: str, path: str,
        query: dict = None, payload: dict = None
    ) -> dict:
        if query is None:
            query = {"token": self.token}
        else:
            query["token"] = self.token
        query = urllib.parse.urlencode(query)
        url = "{}{}?{}".format(self.host, path, query)
        args = {
            "url": url,
            "headers": self.headers,
            "method": method.upper()
        }
        if payload is not None:
            payload = json.dumps(payload).encode('utf-8')
            args["data"] = payload
        else:
            payload = b""
        print(args)
        req = urllib.request.Request(**args)
        try:
            with urllib.request.urlopen(req) as res:
                return self._response_parse(res)
        except APIException as e:
            raise e
        except urllib.error.HTTPError as e:
            raise APIException(e)

    def _response_parse(self, res: http.client.HTTPResponse) -> dict:
        body = res.read().decode("utf-8")
        if body is "" or body is None:
            return {}
        regex = r"(\"[^\":,]+?_id\"):([0-9]+)"
        matches = re.findall(regex, body)
        for m in matches:
            body = body.replace(
                m[0] + ":" + m[1],
                m[0] + ":\""+ m[1] + "\""
            )
        body = json.loads(body)
        status = body.get("status", None)
        if status is None:
            status = body.get("error", None)
        if status == "success":
            return body
        elif status == "error":
            ex = APIException()
            ex.state = res.status
            ex.hdrs = res.getheaders()
            ex.fp = res.fp
            ex.filename = res.url
            ex.msg = body["errors"]
            ex.code = body["errorCode"]
            raise ex
