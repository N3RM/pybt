from datetime import date
from api_wrapper.utils import format_bigtime_date

from api_wrapper.models import Result, Time, StaffTimesheet, ProjectTimesheet

class _Time:
    def __init__(self, method):
        self._endpoint = "Time"
        self._method = method

    def __call__(self, time_id : str = None, time : Time = None, mark_submitted : bool = False) -> Time:
        params = {}
        if time:
            params = {**time}
        if mark_submitted:
            params["marksubmitted"] = "true"
        result: Result = self._method(endpoint=f"{self._endpoint}/{time_id}", params=params)
        return Time(**result.data)

    def _sheet(self, staff_id : str, start_date : date, end_date : date, view : str = "detailed") -> StaffTimesheet:
        params = {}
        params["startdt"] = format_bigtime_date(start_date)
        params["enddt"] = format_bigtime_date(end_date)
        if view:
            params["view"] = view
        result: Result = self._method(endpoint=f"{self._endpoint}/Sheet/{staff_id}", params=params)
        return StaffTimesheet(staffSID=staff_id, start_date=start_date, end_date=end_date, timesheet=[Time(**time) for time in result.data])
    
    def _by_project(self, project_id : str, start_date : date, end_date : date, view : str = "detailed", is_approved : bool = False) -> ProjectTimesheet:
        params = {}
        params["startdt"] = format_bigtime_date(start_date)
        params["enddt"] = format_bigtime_date(end_date)
        if view:
            params["view"] = view
        if is_approved:
            params["isapproved"] = "true"
        result: Result = self._method(endpoint=f"{self._endpoint}/ByProject/{project_id}", params=params)
        return ProjectTimesheet(projectSID=project_id, start_date=start_date, end_date=end_date, timesheet=[Time(**time) for time in result.data])
