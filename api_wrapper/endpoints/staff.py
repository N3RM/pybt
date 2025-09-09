from api_wrapper.models import Result, User

class _Staff:
    def __init__(self, method):
        self._endpoint = "Staff"
        self._method = method

    def __call__(self, show_inactive : bool = False) -> list[User]:
        params = {}
        if show_inactive:
            params["show_inactive"] = "true"
        result: Result = self._method(endpoint=f"{self._endpoint}", params=params)
        return [User(**staff) for staff in result.data]

    def _detail(self, staff_id : str = None, view : str = None, show_all_contacts : bool = False, staff : User = None) -> User | Result:
        params = {}
        if view:
            params["view"] = view
        if show_all_contacts:
            params["showallcontacts"] = "true"
        if staff:
            params = {**staff}
        result: Result = self._method(endpoint=f"{self._endpoint}/Detail/{staff_id}" if staff_id else f"{self._endpoint}/Detail", params=params)
        return User(**result.data) if result.data else f"{result.status_code}: {result.message}"