from api_wrapper import models
from api_wrapper.endpoints import _Picklist, _Project, _Client

class Get:
    def __init__(self, api):
        self._method: callable = api._rest_adapter.get
        self.picklist = self._Get_Picklist(self._method)
        self.project = self._Get_Project(self._method)
        
    class _Get_Picklist(_Picklist):
        def __init__(self, method):
            super().__init__(method=method)

        def projects(self, staff_sid : str = None):
            return self._projects(staff_sid=staff_sid)
        
        def clients(self):
            return self._clients()
        
        def staff(self, show_inactive : bool = False):
            return self._staff(show_inactive)
        
        def all_tasks_by_project(self, project_id : str, budget_type : str = None, show_inactive : bool = False):
            return self._all_tasks_by_project(project_id, budget_type, show_inactive)
        
        def estimates_by_project(self, project_id : str, staff_sid : str = None, budget_type : str = None, show_inactive : bool = False):
            return self._estimates_by_project(project_id, staff_sid, budget_type, show_inactive)
        
        def field_values(self, sid : str, show_inactive : bool = False):
            return self._field_values(sid, show_inactive)
    

    class _Get_Project:
        def __init__(self, method):
            self._project = _Project(method)

        def __call__(self, show_inactive : bool = False) -> models.ProjectList:
            return self._project(show_inactive)

        def detail(self, project_id : str, view : str = None, show_all_contacts : bool = False) -> models.Project:
            return self._project._detail(project_id, view, show_all_contacts)
        
        def contacts(self, project_id : str) -> models.ContactList:
            return self._project._contacts(project_id)
        
        def contact(self, project_id : str, contact_id : str) -> models.Contact:
            return self._project._contact(project_id=project_id, contact_id=contact_id)
        
        def team(self, project_id) -> models.ProjectTeam:
            return self._project._team(project_id=project_id)
        
    class _Get_Client:
        def __init__(self, method):
            self._client = _Client(method)

        def __call__(self, show_inactive : bool = False) -> models.ClientList:
            return self._client(show_inactive)

        def detail(self, client_id : str, view : str = None) -> models.Client:
            return self._client._detail(client_id, view)