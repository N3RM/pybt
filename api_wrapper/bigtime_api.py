from api_wrapper.rest_adapter import RestAdapter
from api_wrapper.methods import Get, Create, Update, Delete


class BigTimeAPI:
    def __init__(
        self,
        api_key: str,
        firm: str,
        hostname: str = "iq.bigtime.net/BigtimeData/api",
        ver: str = "v2",
        ssl_verify: bool = False,
    ) -> None:
        self._rest_adapter = RestAdapter(hostname, api_key, firm, ver, ssl_verify)
        self.get = Get(self)
        self.create = Create(self)
        self.update = Update(self)
        self.delete = Delete(self)