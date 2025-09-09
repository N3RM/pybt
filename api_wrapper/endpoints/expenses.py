from api_wrapper.models import Result

class _Expense:
    def __init__(self, method):
        self._endpoint = "Expense"
        self._method = method

    def __call__(self, show_inactive : bool = False) -> list[Expense]:
        params = {}
        if show_inactive:
            params["show_inactive"] = "true"
        result: Result = self._method(endpoint=f"{self._endpoint}", params=params)
        return [Expense(**expense) for expense in result.data]

    def _detail(self, expense_id : str = None, view : str = None, show_all_contacts : bool = False, expense : Expense = None) -> Expense | Result:
        params = {}
        if view:
            params["view"] = view
        if show_all_contacts:
            params["showallcontacts"] = "true"
        if expense:
            params = {**expense}
        result: Result = self._method(endpoint=f"{self._endpoint}/Detail/{expense_id}" if expense_id else f"{self._endpoint}/Detail", params=params)
        return Expense(**result.data) if result.data else f"{result.status_code}: {result.message}"