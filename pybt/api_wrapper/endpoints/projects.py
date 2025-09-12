from api_wrapper.models import Result, Project, Contact, ProjectTeam, ProjectTeamMember, CustomField

class _Project:
    def __init__(self, method):
        self._endpoint = "Project"
        self._method = method

    def __call__(self, show_inactive : bool = False) -> list[Project]:
        params = {}
        if show_inactive:
            params["show_inactive"] = "true"
        result: Result = self._method(endpoint=f"{self._endpoint}", params=params)
        return [Project(**project) for project in result.data]

    def _detail(self, project_id : str = None, view : str = None, show_all_contacts : bool = False, project : Project = None) -> Project | Result:
        params = {}
        if view:
            params["view"] = view
        if show_all_contacts:
            params["showallcontacts"] = "true"
        if project:
            params = {**project}
        result: Result = self._method(endpoint=f"{self._endpoint}/Detail/{project_id}" if project_id else f"{self._endpoint}/Detail", params=params)
        return Project(**result.data) if result.data else f"{result.status_code}: {result.message}"
    
    def _contacts(self, project_id : str = None) -> list[Contact]:
        params = {}
        params["id"] = project_id
        result: Result = self._method(endpoint=f"{self._endpoint}/Contacts", params=params)
        return [Contact(**contact) for contact in result.data]
    
    def _contact(self, project_id : str = None, contact_id : str = None, show_all : bool = False, contact : Contact = None) -> Contact:
        params = {}
        params["projectsid"] = project_id
        if show_all:
            params["showall"] = "true"
        if contact:
            params = {**contact}
        result: Result = self._method(endpoint=f"{self._endpoint}/Contact/{contact_id}" if contact_id else f"{self._endpoint}/Contact", params=params)
        return Contact(**result.data) if result.data else f"{result.status_code}: {result.message}"
    
    def _team(self, project_id : str = None, project_team : ProjectTeam = None):
        params = {}
        if project_team:
            params = project_team.team_members
        result: Result = self._method(endpoint=f"{self._endpoint}/Team/{project_id}", params=params)
        return ProjectTeam([ProjectTeamMember(**member) for member in result.data], project_id) if result.data else f"{result.status_code}: {result.message}"
    
    def _custom_fields(self, project_id : str = None, custom_fields : list[CustomField] = None):
        params = {}
        if custom_fields:
            params = {"customfields": custom_fields}
        result: Result = self._method(endpoint=f"{self._endpoint}/CustomFields/{project_id}", params=params)
        return [CustomField(**field) for field in result.data]