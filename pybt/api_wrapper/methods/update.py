from api_wrapper.models import Client, Expense, Project, Contact, User, Task, Time, Invoice, ProjectTeam, CustomField
from api_wrapper.endpoints import _Client, _Expense, _Invoice, _Project, _Staff, _Task, _Time


class Update:
    def __init__(self, api):
        self._method: callable = api._rest_adapter.get
        self.client = self._Update_Client(self._method)
        self.expense = self._Update_Expense(self._method)
        self.invoice = self._Update_Invoice(self._method)
        self.project = self._Update_Project(self._method)
        self.staff = self._Update_Staff(self._method)
        self.task = self._Update_Task(self._method)
        self.time = self._Update_Time(self._method)

    class _Update_Client:
        def __init__(self, method):
            self._client = _Client(method)

        def detail(self, client : Client):
            return self._client._detail(client_id=client.id, client=client)
        

    class _Update_Expense:
        def __init__(self, method):
            self._expense = _Expense(method)

        def detail(self, expense : Expense):
            return self._expense._detail(expense_id=expense.id, expense=expense)


    class _Update_Invoice:
        def __init__(self, method):
            self._invoice = _Invoice(method)

        def detail(self, invoice : Invoice):
            return self._invoice._detail(invoice_id=invoice.id, invoice=invoice)
    

    class _Update_Project:
        def __init__(self, method):
            self._project = _Project(method)

        def detail(self, project : Project):
            return self._project._detail(project_id=project.id, project=project)
        
        def contact(self, contact : Contact):
            return self._project._contact(contact_id=contact.id, contact=contact)
        
        def team(self, project_team : ProjectTeam):
            return self._project._team(project_id=project_team.project_id, project_team=project_team)
        
        def custom_field(self, project_id : str, custom_fields : list[CustomField]):
            return self._project._custom_fields(project_id=project_id, custom_fields=custom_fields)


    class _Update_Staff:
        def __init__(self, method):
            self._staff = _Staff(method)
        
        def detail(self, staff : User):
            return self._staff._detail(staff_id=staff.id, staff=staff)


    class _Update_Task:
        def __init__(self, method):
            self._task = _Task(method)

        def detail(self, task : Task):
            return self._task._detail(task_id=task.id, task=task)


    class _Update_Time:
        def __init__(self, method):
            self._time = _Time(method)

        def __call__(self, time : Time, mark_submitted : bool = False):
            return self._time(time_id=time.id, time=time, mark_submitted=mark_submitted)