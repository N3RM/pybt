from datetime import date

from api_wrapper.models import Result, Report
from api_wrapper.utils import format_bigtime_date

class _Report:
    def __init__(self, method):
        self._endpoint = "Report"
        self._method = method

    def _data(self, report_id : str = None, start_date : date = None, end_date : date = None) -> Report | Result:
        params = {}
        if start_date:
            params["startdt"] = format_bigtime_date(start_date)
        if end_date:
            params["enddt"] = format_bigtime_date(end_date)

        result: Result = self._method(endpoint=f"{self._endpoint}/Data/{report_id}", params=params)
        return Report(**result.data)