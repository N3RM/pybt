from api_wrapper.models import Result, Time

class _Time:
    def __init__(self, method):
        self._endpoint = "Time"
        self._method = method

    def __call__(self, show_inactive : bool = False) -> list[Time]:
        params = {}
        if show_inactive:
            params["show_inactive"] = "true"
        result: Result = self._method(endpoint=f"{self._endpoint}", params=params)
        return [Time(**time) for time in result.data]

    def _detail(self, time_id : str = None, view : str = None, show_all_contacts : bool = False, time : Time = None) -> Time | Result:
        params = {}
        if view:
            params["view"] = view
        if show_all_contacts:
            params["showallcontacts"] = "true"
        if time:
            params = {**time}
        result: Result = self._method(endpoint=f"{self._endpoint}/Detail/{time_id}" if time_id else f"{self._endpoint}/Detail", params=params)
        return Time(**result.data) if result.data else f"{result.status_code}: {result.message}"