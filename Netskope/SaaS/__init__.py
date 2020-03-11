from datetime import datetime
from ..client import Client
from ..Utils import validation
from ..Utils import get_arguments
import sys


class SaaS(Client):
    """
    @namespace  Netskope.SaaS
    """
    @validation
    def events(
        self, type: str = None, timeperiod: int = None,
        starttime: datetime = None, endtime: datetime = None,
        insertionstarttime: datetime = None, insertionendtime: datetime = None,
        limit: int = None, skip: int = None
    ) -> list:
        query = get_arguments(locals())
        path = sys._getframe().f_code.co_name
        response = self.request(method="get", path=path, query=query)
        return response.get("data", [])

    @validation
    def alerts(
        self, type: str = None, acked: bool = None, timeperiod: int = None,
        starttime: datetime = None, endtime: datetime = None,
        insertionstarttime: datetime = None, insertionendtime: datetime = None,
        limit: int = None, skip: int = None
    ) -> list:
        query = get_arguments(locals())
        path = sys._getframe().f_code.co_name
        response = self.request(method="get", path=path, query=query)
        return response.get("data", [])

    @validation
    def report(
        self, type: str = None, groupby: str = None, timeperiod: int = None,
        starttime: datetime = None, endtime: datetime = None,
        limit: int = None, skip: int = None
    ) -> list:
        query = get_arguments(locals())
        path = sys._getframe().f_code.co_name
        response = self.request(method="get", path=path, query=query)
        return response.get("data", [])

    def steeringconfiglist(self) -> list:
        query = get_arguments(locals())
        path = sys._getframe().f_code.co_name
        response = self.request(method="get", path=path, query=query)
        return response.get("data", [])

    @validation
    def steeringconfig(
        self, config: int = None, config_id: str = None,
        limit: int = None, skip: int = None
    ) -> list:
        query = get_arguments(locals())
        path = sys._getframe().f_code.co_name
        response = self.request(method="get", path=path, query=query)
        return response.get("data", [])

    @validation
    def userconfig(self, email: str = None, configtype: str = None) -> list:
        query = get_arguments(locals())
        path = sys._getframe().f_code.co_name
        response = self.request(method="get", path=path, query=query)
        return response.get("data", [])

    def uploadtoken(self) -> str:
        query = get_arguments(locals())
        path = sys._getframe().f_code.co_name
        response = self.request(method="get", path=path, query=query)
        return response.get("data", "")

    @validation
    def quarantine(
        self, op: str = None, quarantine_profile_id: str = None,
        starttime: datetime = None, endtime: datetime = None,
        file_id: str = None, action: str = None
    ) -> list:
        query = get_arguments(locals())
        path = sys._getframe().f_code.co_name
        response = self.request(method="get", path=path, query=query)
        return response.get("data", [])

    @validation
    def legalhold(
        self, op: str = None, legalhold_profile_id: str = None,
        starttime: datetime = None, endtime: datetime = None,
        file_id: str = None, action: str = None, type: str = None
    ) -> list:
        query = get_arguments(locals())
        path = sys._getframe().f_code.co_name
        response = self.request(method="get", path=path, query=query)
        return response.get("data", [])

    def ackanomalies(self, users: list=[]) -> str:
        query = get_arguments(locals())
        path = sys._getframe().f_code.co_name
        response = self.request(method="get", path=path, query=query)
        return response.get("data", [])

    def ackcompromisedcred(self, users: list=[]) -> str:
        query = get_arguments(locals())
        path = sys._getframe().f_code.co_name
        response = self.request(method="get", path=path, query=query)
        return response.get("data", [])
