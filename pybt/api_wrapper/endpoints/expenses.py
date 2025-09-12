from datetime import date

from api_wrapper.models import Result, Expense, ExpenseReport
from api_wrapper.utils import format_bigtime_date

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
    
    def _report(self, report_id : str = "0", staff_id : str = None, view : str = None) -> ExpenseReport:
        params = {}
        if staff_id:
            params["staffsid"] = staff_id
        if view:
            params["view"] = view
        result: Result = self._method(endpoint=f"{self._endpoint}/Report/{report_id}", params=params)
        return ExpenseReport(**result.data) if result.data else result
    
    def _report_by_filter(self, start_date : date = None, end_date : date = None, staff_ids : list[str] = None, project_ids : list[str] = None, view : str = "Basic", show_approval : bool = False):
        params = {}
        if start_date:
            params["mindate"] = format_bigtime_date(start_date)
        if end_date:
            params["maxdate"] = format_bigtime_date(end_date)
        if staff_ids:
            params["staffsids"] = staff_ids
        if project_ids:
            params["projectsids"] = project_ids
        if view:
            params["view"] = view
        if show_approval:
            params["showapproval"] = "true"
        result: Result = self._method(endpoint=f"{self._endpoint}/ReportByFilter", params=params)
        return [Expense(**expense) for expense in result.data]

    def _reports(self, staff_id : str = None, show_all : bool = False) -> list[ExpenseReport]:
        params = {}
        if staff_id:
            params["staffsid"] = staff_id
        if show_all:
            params["showall"] = "true"
        result: Result = self._method(endpoint=f"{self._endpoint}/Reports", params=params)
        return [ExpenseReport(**report) for report in result.data]