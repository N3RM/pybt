from api_wrapper.models import Result, Task, TaskBudgetData

class _Task:
    def __init__(self, method):
        self._endpoint = "Task"
        self._method = method

    def _detail(self, task_id : str = None, view : str = None, task : Task = None) -> Task | Result:
        params = {}
        if view:
            params["view"] = view
        if task:
            params = {**task}

        result: Result = self._method(endpoint=f"{self._endpoint}/Detail/{task_id}" if task_id else f"{self._endpoint}/Detail", params=params)
        return Task(**result.data) if result.data else f"{result.status_code}: {result.message}"
    
    def _list_by_project(self, project_id : str = None, show_completed : bool = False):
        params = {}
        if show_completed:
            params["showcompleted"] = "true"
        
        result: Result = self._method(endpoint=f"{self._endpoint}/ListByProject/{project_id}", params=params)
        return [Task(**task) for task in result.data]
    
    def _budget_status_by_project(self, project_id : str = None):
        params = {}
        
        result: Result = self._method(endpoint=f"{self._endpoint}/BudgetStatusByProject/{project_id}", params=params)
        return [TaskBudgetData(**budget_status) for budget_status in result.data]