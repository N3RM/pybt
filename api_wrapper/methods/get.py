from datetime import date

from api_wrapper.endpoints import _Client, _Expense, _Invoice, _Payment, _Picklist, _Project, _Report, _Staff, _Task, _Time

class Get:
    def __init__(self, api):
        self._method: callable = api._rest_adapter.get
        self.client = self._Get_Client(self._method)
        self.expense = self._Get_Expense(self._method)
        self.invoice = self._Get_Invoice(self._method)
        self.payment = self._Get_Payment(self._method)
        self.picklist = self._Get_Picklist(self._method)
        self.project = self._Get_Project(self._method)
        self.report = self._Get_Report(self._method)
        self.staff = self._Get_Staff(self._method)
        self.task = self._Get_Task(self._method)
        self.time = self._Get_Time(self._method)

    class _Get_Client:
        def __init__(self, method):
            self._client = _Client(method)

        def __call__(self, show_inactive : bool = False):
            return self._client(show_inactive)

        def detail(self, client_id : str, view : str = None):
            return self._client._detail(client_id, view)
        

    class _Get_Expense:
        def __init__(self, method):
            self._expense = _Expense(method)

        def detail(self, expense_id : str):
            return self._expense._detail(expense_id=expense_id)
        
        def report(self, report_id : str = "0", staff_id : str = None, view : str = "Detailed"):
            return self._expense._report(report_id=report_id, staff_id=staff_id, view=view)
        
        def reports(self, staff_id : str = None, show_all : bool = False):
            return self._expense._reports(staff_id=staff_id, show_all=show_all)


    class _Get_Invoice:
        def __init__(self, method):
            self._invoice = _Invoice(method)

        def history(self, start_date : date, end_date : date):
            return self._invoice._history(start_date=start_date, end_date=end_date)

        def drafts(self, start_date : date = None, end_date : date = None):
            return self._invoice._drafts(start_date=start_date, end_date=end_date)
        
        def by_client(self, client_id : str, start_date : date = None, end_date : date = None):
            return self._invoice._invoices_by_client(client_id=client_id, start_date=start_date, end_date=end_date)
        
        def detail(self, invoice_id : str):
            return self._invoice._detail(invoice_id=invoice_id)


    class _Get_Payment:
        def __init__(self, method):
            self._payment = _Payment(method)

        
    class _Get_Picklist:
        def __init__(self, method):
            self._picklist = _Picklist(method)

        def projects(self, staff_sid : str = None):
            return self._picklist._projects(staff_sid=staff_sid)
        
        def clients(self):
            return self._picklist._clients()
        
        def staff(self, show_inactive : bool = False):
            return self._picklist._staff(show_inactive)
        
        def all_tasks_by_project(self, project_id : str, budget_type : str = None, show_inactive : bool = False):
            return self._picklist._all_tasks_by_project(project_id, budget_type, show_inactive)
        
        def estimates_by_project(self, project_id : str, staff_sid : str = None, budget_type : str = None, show_inactive : bool = False):
            return self._picklist._estimates_by_project(project_id, staff_sid, budget_type, show_inactive)
        
        def field_values(self, sid : str, show_inactive : bool = False):
            return self._picklist._field_values(sid, show_inactive)
    

    class _Get_Project:
        def __init__(self, method):
            self._project = _Project(method)

        def __call__(self, show_inactive : bool = False):
            return self._project(show_inactive)

        def detail(self, project_id : str, view : str = "Detailed", show_all_contacts : bool = False):
            return self._project._detail(project_id, view, show_all_contacts)
        
        def contacts(self, project_id : str):
            return self._project._contacts(project_id)
        
        def contact(self, project_id : str, contact_id : str):
            return self._project._contact(project_id=project_id, contact_id=contact_id)
        
        def team(self, project_id):
            return self._project._team(project_id=project_id)
        
    
    class _Get_Report:
        def __init__(self, method):
            self._report = _Report(method)

        def __call__(self, report_id):
            return self._report._data(report_id=report_id)


    class _Get_Staff:
        def __init__(self, method):
            self._staff = _Staff(method)

        def __call__(self, show_inactive : bool = False):
            return self._staff(show_inactive=show_inactive)
        
        def detail(self, staff_id : str, view : str = "Detailed"):
            return self._staff._detail(staff_id=staff_id, view=view)


    class _Get_Task:
        def __init__(self, method):
            self._task = _Task(method)

        def detail(self, task_id : str, view : str = None):
            return self._task._detail(task_id=task_id, view=view)
        
        def list_by_project(self, project_id : str, show_completed : bool = False):
            return self._task._list_by_project(project_id=project_id, show_completed=show_completed)
        
        def budget_status_by_project(self, project_id : str):
            return self._task._budget_status_by_project(project_id=project_id)


    class _Get_Time:
        def __init__(self, method):
            self._time = _Time(method)

        def __call__(self, time_id : str):
            return self._time(id=time_id)
        
        def sheet(self, staff_id : str, start_date : date, end_date : date, view : str = "Detailed"):
            return self._time._sheet(staff_id=staff_id, start_date=start_date, end_date=end_date, view=view)
        
        def by_project(self, project_id : str, start_date : date, end_date : date, view : str = "Detailed", is_approved : bool = False):
            return self._time._by_project(project_id=project_id, start_date=start_date, end_date=end_date, view=view, is_approved=is_approved)