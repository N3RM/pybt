from api_wrapper.models import Result, Expense, ExpenseReport

class _Expense:
    def __init__(self, method):
        self._endpoint = "Expense"
        self._method = method

    def _detail(self, expense_id : str = None, expense : Expense = None) -> Expense | str:
        params = {}
        if expense:
            params = {**expense}
        result: Result = self._method(endpoint=f"{self._endpoint}/Detail/{expense_id}" if expense_id else f"{self._endpoint}/Detail", params=params)
        return Expense(**result.data) if result.data else f"{result.status_code}: {result.message}"
    
    def _report(self, report_id : str = "0", staff_id : str = None, view : str = "Detailed") -> ExpenseReport:
        params = {}
        if staff_id:
            params["staffsid"] = staff_id
        if view:
            params["view"] = view
        result: Result = self._method(endpoint=f"{self._endpoint}/Report/{report_id}", params=params)
        return ExpenseReport(**result.data)
    
    def _reports(self, staff_id : str = None, show_all : bool = False) -> list[ExpenseReport]:
        params = {}
        if staff_id:
            params["staffsid"] = staff_id
        if show_all:
            params["showall"] = "true"
        result: Result = self._method(endpoint=f"{self._endpoint}/Reports", params=params)
        return [ExpenseReport(**report) for report in result.data]