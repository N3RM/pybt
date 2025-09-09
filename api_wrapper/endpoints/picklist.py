from api_wrapper.models import Result, Picklist, PicklistProject

class _Picklist:
    def __init__(self, method):
        self._endpoint = "Picklist"
        self._method = method

    def _projects(self, staff_sid : str = None):
        """
        Get a list of projects that the current user has permissions to see.
        BigTime API docs say that you can include staffsid to see only projects that staffer is on,
        but testing shows that it only returns a list of all projects that the current user can see
        regardless of if the staffsid is included or not.
        """
        params = {}
        if staff_sid:
            params["staffsid"] = staff_sid
        result: Result = self._method(endpoint=f"{self._endpoint}/Projects", params=params)
        return Picklist([PicklistProject(**project) for project in result.data])
    
    def _clients(self):
        result: Result = self._clients(endpoint=f"{self._endpoint}/Clients", params=None)
        return result # modify to put data into model class before returning
    
    def _staff(self, show_inactive : bool = False):
        params = {}
        if show_inactive:
            params["showinactive"] = "true"
        result: Result = self._method(endpoint=f"{self._endpoint}/Staff", params=params)
        return result # modify to put data into model class before returning
    
    def _all_tasks_by_project(self, project_sid : str, budget_type : str = None, filter_id : str = None, show_inactive : bool = False):
        params = {}
        if budget_type:
            params["budgettype"] = budget_type
        if show_inactive:
            params["showinactive"] = "true"

        result: Result = self._method(endpoint=f"{self._endpoint}/AllTasksByProject/{project_sid}", params=params)
        return result # modify to put data into model class before returning
    
    def _estimates_by_project(self, project_sid : str, staff_sid : str = None, budget_type : str = None, show_inactive : bool = False):
        params = {}
        if staff_sid:
            params["staffsid"] = staff_sid
        if budget_type:
            params["budgettype"] = budget_type
        if show_inactive:
            params["showinactive"] = "true"

        result: Result = self._method(endpoint=f"{self._endpoint}/EstimatesByProjects/{project_sid}", params=params)
        return result # modify to put data into model class before returning
    
    def _field_values(self, sid : str, show_inactive : bool = False):
        params = {}
        params["sid"] = sid
        if show_inactive:
            params = {"showinactive": "true"}
        result: Result = self._method(endpoint=f"{self._endpoint}/FieldValues", params=params)
        return result # modify to put data into model class before returning