import urllib
import json


class APIException(urllib.error.HTTPError):
    def __init__(self, e: urllib.error.HTTPError = None):
        super()
        if  e is not None:
            self.state = e.code
            self.hdrs = e.hdrs
            self.fp = e.fp
            self.filename = e.filename
            body = e.read().decode("utf-8")
            body = json.loads(body)
            self.msg = body["errors"]
            self.code = body["errorCode"]
            self.code = body["errorCode"]

    def __str__(self):
        msg = None
        if isinstance(self.msg, list):
            if len(self.msg) == 1:
                msg = self.msg[0]
            elif len(self.msg) >= 1:
                msg = "/".join(self.msg)
        else:
            msg = self.msg
        return json.dumps({
            "message": msg,
            "code": self.code,
            "status": self.state,
            "filename": self.filename
        })
