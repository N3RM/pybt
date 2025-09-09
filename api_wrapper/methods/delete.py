class Delete:
    def __init__(self, api):
        self._method: callable = api._rest_adapter.delete