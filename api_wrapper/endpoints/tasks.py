from api_wrapper.models import Result, Task

class _Task:
    def __init__(self, method):
        self._endpoint = "Task"
        self._method = method

    def __call__(self, show_inactive : bool = False) -> list[Task]:
        params = {}
        if show_inactive:
            params["show_inactive"] = "true"
        result: Result = self._method(endpoint=f"{self._endpoint}", params=params)
        return [Task(**task) for task in result.data]

    def _detail(self, task_id : str = None, view : str = None, show_all_contacts : bool = False, task : Task = None) -> Task | Result:
        params = {}
        if view:
            params["view"] = view
        if show_all_contacts:
            params["showallcontacts"] = "true"
        if task:
            params = {**task}
        result: Result = self._method(endpoint=f"{self._endpoint}/Detail/{task_id}" if task_id else f"{self._endpoint}/Detail", params=params)
        return Task(**result.data) if result.data else f"{result.status_code}: {result.message}"