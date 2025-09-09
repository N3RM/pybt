from api_wrapper.models import Result, Report

class _Report:
    def __init__(self, method):
        self._endpoint = "Report"
        self._method = method

    def __call__(self, show_inactive : bool = False) -> list[Report]:
        params = {}
        if show_inactive:
            params["show_inactive"] = "true"
        result: Result = self._method(endpoint=f"{self._endpoint}", params=params)
        return [Report(**report) for report in result.data]

    def _detail(self, report_id : str = None, view : str = None, show_all_contacts : bool = False, report : Report = None) -> Report | Result:
        params = {}
        if view:
            params["view"] = view
        if show_all_contacts:
            params["showallcontacts"] = "true"
        if report:
            params = {**report}
        result: Result = self._method(endpoint=f"{self._endpoint}/Detail/{report_id}" if report_id else f"{self._endpoint}/Detail", params=params)
        return Report(**result.data) if result.data else f"{result.status_code}: {result.message}"