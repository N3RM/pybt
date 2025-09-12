from api_wrapper.models import Result, Client

class _Client:
    def __init__(self, method):
        self._endpoint = "Client"
        self._method = method

    def __call__(self, show_inactive : bool = False) -> list[Client]:
        params = {}
        if show_inactive:
            params["show_inactive"] = "true"
        result: Result = self._method(endpoint=f"{self._endpoint}", params=params)
        return [Client(**client) for client in result.data]
    
    def _detail(self, client_id : str = None, view : str = None, client : Client = None) -> Client | str:
        params = {}
        if view:
            params["view"] = view
        if client:
            params = {**client}
        result: Result = self._method(endpoint=f"{self._endpoint}/Detail/{client_id}" if client_id else f"{self._endpoint}/Detail", params=params)
        return Client(**result.data) if result.data else f"{result.status_code}: {result.message}"