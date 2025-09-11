from datetime import date
from api_wrapper.exceptions import BigTimeAPIException

from api_wrapper.rest_adapter import RestAdapter
from api_wrapper.methods import Get, Create, Update, Delete
from api_wrapper.utils import format_bigtime_date, get_month_end_date, get_month_start_date, get_last_month_end_date, get_last_month_start_date, get_this_month_end_date, get_this_month_start_date, PicklistFieldValueChoices, ViewChoices


class BigTimeAPI:
    def __init__(
        self,
        api_key: str,
        firm: str,
        hostname: str = "iq.bigtime.net/BigtimeData/api",
        ver: str = "v2",
        ssl_verify: bool = False,
    ) -> None:
        self._rest_adapter = RestAdapter(hostname, api_key, firm, ver, ssl_verify)
        self._get = Get(self)
        self._create = Create(self)
        self._update = Update(self)
        self._delete = Delete(self)

    #### Staff Timesheets

    def get_staff_timesheet(self, staff_id : str, start_date : date, end_date : date):
        return self._get.time.sheet(staff_id=staff_id, start_date=start_date, end_date=end_date, view=ViewChoices.DETAILED)

    def get_month_staff_timesheet(self, staff_id : str, month : int, year : int):
        if month < 1 or month > 12:
            raise BigTimeAPIException("Only 1-12 are valid values for month")
        return self.get_staff_timesheet(staff_id=staff_id, start_date=get_month_start_date(month=month, year=year), end_date=get_month_end_date(month=month, year=year))
    
    def get_this_month_staff_timesheet(self, staff_id : str):
        return self.get_staff_timesheet(staff_id=staff_id, start_date=get_this_month_start_date(), end_date=get_this_month_end_date())
    
    def get_last_month_staff_timesheet(self, staff_id : str):
        return self.get_staff_timesheet(staff_id=staff_id, start_date=get_last_month_start_date(), end_date=get_last_month_end_date())
    
    def get_all_staff_timesheets(self, start_date : date, end_date : date):
        staff_list = self._get.picklist.staff()
        return [self.get_staff_timesheet(staff_id=staff.id, start_date=start_date, end_date=end_date) for staff in staff_list]
    
    def get_month_all_staff_timesheets(self, month : int, year : int):
        return self.get_all_staff_timesheets(start_date=get_month_start_date(month, year), end_date=get_month_end_date(month, year))
    
    def get_this_month_all_staff_timesheets(self):
        return self.get_all_staff_timesheets(start_date=get_this_month_start_date(), end_date=get_this_month_end_date())
    
    def get_last_month_all_staff_timesheets(self):
        return self.get_all_staff_timesheets(start_date=get_last_month_start_date(), end_date=get_last_month_end_date())

    #### Project Timesheets

    def get_project_timesheet(self, project_id : str, start_date : date, end_date : date):
        return self._get.time.sheet(project_id=project_id, start_date=start_date, end_date=end_date, view=ViewChoices.DETAILED)
    
    def get_month_project_timesheet(self, project_id : str, month : int, year : int):
        if month < 1 or month > 12:
            raise BigTimeAPIException("Only 1-12 are valid values for month")
        return self.get_project_timesheet(project_id=project_id, start_date=get_month_start_date(month=month, year=year), end_date=get_month_end_date(month=month, year=year))

    def get_this_month_project_timesheet(self, project_id : str):
        return self.get_project_timesheet(project_id=project_id, start_date=get_this_month_start_date(), end_date=get_this_month_end_date())
    
    def get_last_month_project_timesheet(self, project_id : str):
        return self.get_project_timesheet(project_id=project_id, start_date=get_last_month_start_date(), end_date=get_last_month_end_date())
    
    def get_all_project_timesheets(self, start_date : date, end_date : date):
        project_list = self._get.picklist.projects()
        return [self.get_project_timesheet(project_id=project.id, start_date=start_date, end_date=end_date) for project in project_list]
    
    def get_month_all_project_timesheets(self, month : int, year : int):
        return self.get_all_project_timesheets(start_date=get_month_start_date(month, year), end_date=get_month_end_date(month, year))
    
    def get_this_month_all_project_timesheets(self):
        return self.get_all_project_timesheets(start_date=get_this_month_start_date(), end_date=get_this_month_end_date())
    
    def get_last_month_all_project_timesheets(self):
        return self.get_all_project_timesheets(start_date=get_last_month_start_date(), end_date=get_last_month_end_date())