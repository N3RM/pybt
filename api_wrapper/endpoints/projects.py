from api_wrapper.models import Result, Project

class _Project:
    def __init__(self, method):
        self._endpoint = "Project"
        self._method = method

    def __call__(self, show_inactive : bool = False) -> Project:
        params = None
        if show_inactive:
            params["show_inactive"] = "true"
        result: Result = self._method(endpoint=f"{self._endpoint}/", params=params)
        return Project(**result.data)

    def _detail(self, project_sid : str = None, view : str = None, show_all_contacts : bool = False) -> Project | Result:
        """
        Get a list of projects that the current user has permissions to see.
        BigTime API docs say that you can include staffsid to see only projects that staffer is on,
        but testing shows that it only returns a list of all projects that the current user can see
        regardless of if the staffsid is included or not.
        """
        params = None
        if view:
            params["view"] = view
        if show_all_contacts:
            params["showallcontacts"] = "true"
        result: Result = self._method(endpoint=f"{self._endpoint}/Detail/{project_sid}" if project_sid else f"{self._endpoint}/Detail/", params=params)
        return Project(**result.data) if result.data else result
    
    