from api_wrapper.models import Picklist, Result, PicklistIdName, PicklistProject, Timesheet, StaffTimesheet, Time, Project, Contact, ProjectTeamMember, Task
from api_wrapper.rest_adapter import RestAdapter
from api_wrapper.endpoints import PicklistEndPoint
from datetime import date
import calendar


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
        self.get = self._Get(self)
        self.create = self._Create(self)
        self.update = self._Update(self)
        self.delete = self._Delete(self)

    class _Get:
        def __init__(self, api):
            self.call: callable = api._rest_adapter.get
            self.picklist = self._Picklist(self.call)
            
        class _Picklist(PicklistEndPoint):
            def __init__(self, method):
                self.endpoint = "Picklist"
                super().__init__(method)

            def projects(self, staff_sid : str = None):
                """
                Get a list of projects that the current user has permissions to see.
                BigTime API docs say that you can include staffsid to see only projects that staffer is on,
                but testing shows that it only returns a list of all projects that the current user can see
                regardless of if the staffsid is included or not.
                """
                result = self._projects(endpoint=f"{self.endpoint}/projects/", params={"staffsid": staff_sid} if staff_sid else None, data=None)
                return Picklist([PicklistProject(**project) for project in result])
    
    class _Create:
        def __init__(self, api):
            self.call = api._rest_adapter.post
    
    class _Update:
        def __init__(self, api):
            self.call = api._rest_adapter.post
    
    class _Delete:
        def __init__(self, api):
            self.call = api._rest_adapter.delete

    ### Helper ###

    def _get_month_start_date(self) -> date:
        return date.today().replace(day=1)

    def _get_month_end_date(self) -> date:
        return date.today().replace(
            day=calendar.monthrange(date.today().year, date.today().month)[1]
        )

    def _format_bigtime_date(self, dt: date) -> str:
        return dt.strftime("%Y-%m-%d")
    
    class Async:
        def __init__(self, api):
            self.api = api
            self.endpoint = "Async"

        
        
        def submit_time_sheet(): ...
        def submit_time_sheet_signed(): ...
        def resubmit_expense_report(): ...
        def resubmit_time(): ...
        def resubmit_all_time_by_staffer(): ...
        def submit_expenses(): ...
        def post_timesheet(): ...
        def post_expense_report(): ...
        def post_invoice(): ...
        def import_qb_time(): ...
        def import_qb_invoices(): ...

    def get_picklist_clients(self) -> Picklist:
        result = self._rest_adapter.get(endpoint="picklist/clients/")
        picklist = Picklist([PicklistIdName(**client) for client in result.data])
        return picklist

    def get_picklist_staff(self) -> Picklist:
        result = self._rest_adapter.get(endpoint="picklist/staff/")
        picklist = Picklist([PicklistIdName(**staff) for staff in result.data])
        return picklist

    def get_picklist_all_tasks_by_project(self, project_sid: str) -> Picklist:
        result = self._rest_adapter.get(
            endpoint=f"picklist/AllTasksByProject/{project_sid}/"
        )
        picklist = Picklist([PicklistIdName(**task) for task in result.data])
        return picklist

    def get_lookup_project_team_roles(self) -> Picklist:
        result = self._rest_adapter.get(
            endpoint="picklist/FieldValues/LookupProjectTeamRoles/"
        )
        picklist = Picklist([PicklistIdName(**role) for role in result.data])
        return picklist

    ### Timesheets ###

    def get_staff_time_sheet(
        self,
        staff_sid: str,
        start_date: str,
        end_date: str,
    ) -> Timesheet:
        staff_timesheet = StaffTimesheet(
            staffSID=staff_sid, start_date=start_date, end_date=end_date
        )
        result = self._rest_adapter.get(
            endpoint=f"time/sheet/{staff_sid}/",
            params={"StartDt": start_date, "EndDt": end_date, "View": "Detailed"},
        )
        timesheet_data = [Time(**time) for time in result.data]
        staff_timesheet.timesheet = timesheet_data
        return staff_timesheet

    def get_current_month_timesheet(
        self,
        staff_sid: str,
    ) -> Timesheet:
        return self.get_staff_time_sheet(
            staff_sid,
            self._format_bigtime_date(self._get_month_start_date()),
            self._format_bigtime_date(self._get_month_end_date()),
        )

    def get_time_by_project(
        self,
        project_sid: str,
        start_date: str,
        end_date: str,
    ) -> Result:
        result = self._rest_adapter.get(
            endpoint=f"time/byproject/{project_sid}/",
            params={"StartDt": start_date, "EndDt": end_date, "View": "Detailed"},
        )
        print(f"Format result:\n{result.data}")
        return result

    ### Expenses ###

    def get_expense_reports(self):
        result = self._rest_adapter.get(
            endpoint="expense/reports/", params={"showAll": "True"}
        )
        print(f"Format result:\n{result.data}")
        return result

    ### Projects ###

    def get_project_detail(self, ProjectSid: str, show_contacts = None):
        result = self._rest_adapter.get(
            endpoint=f"project/detail/{ProjectSid}/",
            params={"View": "Detailed", "ShowAllContacts": show_contacts},
        )
        print(f"Format result:\n{result.data}")
        return result

    def update_project(self, ProjectSid: str, Data: Project):
        result = self._rest_adapter.post(
            endpoint=f"project/detail/{ProjectSid}", data=Data.__dict__
        )
        print(f"Format result:\n{result.data}")
        return result

    def get_project_contacts(self, ProjectSid: str):
        result = self._rest_adapter.get(endpoint=f"project/contacts/{ProjectSid}/")
        print(f"Format result:\n{result.data}")
        return result

    def create_project_contact(self, ProjectSid: str, contact: Contact):
        result = self._rest_adapter.post(
            endpoint=f"project/detail/{ProjectSid}", data=contact.__dict__
        )
        print(f"Format result:\n{result.data}")
        return result

    def delete_project_contact(self, ProjectSid: str, ContactSid: str):
        result = self._rest_adapter.delete(
            endpoint=f"project/contact/{ContactSid}", params={"ProjectSid": ProjectSid}
        )
        print(f"Format result:\n{result.data}")
        return result

    def get_project_team(self, ProjectSid: str):
        result = self._rest_adapter.get(endpoint=f"project/team/{ProjectSid}/")
        print(f"Format result:\n{result.data}")
        return result

    def update_project_team(self, ProjectSid: str, TeamList: list[ProjectTeamMember]):
        result = self._rest_adapter.post(
            endpoint=f"project/team/{ProjectSid}",
            data=[member.__dict__ for member in TeamList],
        )
        print(f"Format result:\n{result.data}")
        return result

    # def delete_project_contact(self, ProjectSid: str, ContactSid: str):
    #     result = self._rest_adapter.delete(
    #         endpoint=f"project/contact/{ContactSid}", params={"ProjectSid": ProjectSid}
    #     )
    #     print(f"Format result:\n{result.data}")
    #     return result

    def get_project_customfields(self, ProjectSid: str):
        result = self._rest_adapter.get(endpoint=f"project/customfields/{ProjectSid}/")
        print(f"Format result:\n{result.data}")
        return result

    def get_project_rates(self, ProjectSid: str):
        result = self._rest_adapter.get(endpoint=f"project/rates/{ProjectSid}/")
        print(f"Format result:\n{result.data}")
        return result

    def create_project_rate(
        self, ProjectSid: str, StaffSid: str, TaskSid: str, RateVal: str
    ):
        result = self._rest_adapter.post(endpoint="project/rate/", data={})
        print(f"Format result:\n{result.data}")
        return result

    ### Clients ###

    def get_client_list(self, show_inactive: bool = False):
        result = self._rest_adapter.get(
            endpoint="client/", params={"ShowInactive": str(show_inactive)}
        )
        print(f"Format result:\n{result.data}")
        return result

    def get_client_detail(self, ClientSid):
        result = self._rest_adapter.get(
            endpoint=f"client/detail/{ClientSid}/", params={"View": "Detailed"}
        )
        print(f"Format result:\n{result.data}")
        return result

    def delete_client(self, ClientSid):
        result = self._rest_adapter.delete(endpoint=f"client/detail/{ClientSid}/")
        print(f"Format result:\n{result.data}")
        return result

    ### Tasks ###

    def get_task_list(self, ProjectSid: str, show_inactive: bool = False):
        result = self._rest_adapter.get(
            endpoint=f"task/ListByProject/{ProjectSid}/",
            params={"ShowInactive": str(show_inactive)},
        )
        print(f"Format result:\n{result.data}")
        return result

    def get_task_detail(self, TaskSid: str):
        result = self._rest_adapter.get(
            endpoint=f"task/detail/{TaskSid}/", params={"View": "Detailed"}
        )
        print(f"Format result:\n{result.data}")
        return result

    def create_task(self, task: Task):
        result = self._rest_adapter.post(endpoint="task/detail", data=task.__dict__)
        print(f"Format result:\n{result.data}")
        return result

    def update_task(self, TaskSid: str, task: Task):
        result = self._rest_adapter.post(
            endpoint=f"task/detail/{TaskSid}", data=task.__dict__
        )
        print(f"Format result:\n{result.data}")
        return result

    def get_task_budget_status_by_project(self, ProjectSid):
        result = self._rest_adapter.get(
            endpoint=f"task/BudgetStatusByProject/{ProjectSid}"
        )
        print(f"Format result:\n{result.data}")
        return result

    ### Invoices ###

    def get_invoice_history(self, StartDt, EndDt):
        result = self._rest_adapter.get(
            endpoint="invoice/history/", params={"startDt": StartDt, "endDt": EndDt}
        )
        print(f"Format result:\n{result.data}")
        return result

    def get_invoice_drafts(self, StartDt, EndDt):
        result = self._rest_adapter.get(
            endpoint="invoice/drafts/", params={"startDt": StartDt, "endDt": EndDt}
        )
        print(f"Format result:\n{result.data}")
        return result

    def get_invoice_by_client(self, ClientSid, StartDt, EndDt):
        result = self._rest_adapter.get(
            endpoint="invoice/drafts/",
            params={"clientid": ClientSid, "startDt": StartDt, "endDt": EndDt},
        )
        print(f"Format result:\n{result.data}")
        return result

    def get_invoice_detail(self, InvoiceSid):
        result = self._rest_adapter.get(endpoint=f"invoice/detail/{InvoiceSid}")
        print(f"Format result:\n{result.data}")
        return result

    def create_invoice(self, ProjectSid: str, InvoiceType: str):
        result = self._rest_adapter.post(
            endpoint="invoice/create",
            params={"projectSid": ProjectSid, "invoiceType": InvoiceType},
        )
        print(f"Format result:\n{result.data}")
        return result

    ### Payments ###

    def get_payment_history(self, StartDt, EndDt):
        result = self._rest_adapter.get(
            endpoint="payment/history/", params={"startDt": StartDt, "endDt": EndDt}
        )
        print(f"Format result:\n{result.data}")
        return result

    ### Reports ###

    def get_report(self, ReportSid):
        result = self._rest_adapter.get(endpoint=f"report/data/{ReportSid}/")
        print(f"Format result:\n{result.data}")
        return result

    def post_report_options(self, ReportSid, **options):
        result = self._rest_adapter.get(
            endpoint=f"report/data/{ReportSid}/", params=options
        )
        print(f"Format result:\n{result.data}")
        return result

    ### Staff ###

    def get_staff_list(self, show_inactive: bool = False):
        result = self._rest_adapter.get(
            endpoint="staff/", params={"ShowInactive": show_inactive}
        )
        print(f"Format result:\n{result.data}")
        return result

    def get_staff_detail(self, StaffSid):
        result = self._rest_adapter.get(
            endpoint=f"client/detail/{StaffSid}/", params={"View": "Detailed"}
        )
        print(f"Format result:\n{result.data}")
        return result
