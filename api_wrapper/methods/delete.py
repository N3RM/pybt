from api_wrapper.endpoints import _Client, _Project


class Delete:
    def __init__(self, api):
        self._method: callable = api._rest_adapter.get
        self.client = self._Delete_Client(self._method)
        self.project = self._Delete_Project(self._method)


    class _Delete_Client:
        def __init__(self, method):
            self._client = _Client(method)

        def detail(self, client_id : str):
            return self._client._detail(client_id=client_id)


    class _Delete_Project:
        def __init__(self, method):
            self._project = _Project(method)

        def contact(self, project_id : str, contact_id : str):
            return self._project._contact(project_id=project_id, contact_id=contact_id)