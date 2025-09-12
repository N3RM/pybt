from api_wrapper.models import Client, Expense, Project, Contact, User, Task, Time
from api_wrapper.endpoints import _Client, _Expense, _Invoice, _Project, _Staff, _Task, _Time

class Create:
    def __init__(self, api):
        self._method: callable = api._rest_adapter.get
        self.client = self._Create_Client(self._method)
        self.expense = self._Create_Expense(self._method)
        self.invoice = self._Create_Invoice(self._method)
        self.project = self._Create_Project(self._method)
        self.staff = self._Create_Staff(self._method)
        self.task = self._Create_Task(self._method)
        self.time = self._Create_Time(self._method)

    class _Create_Client:
        def __init__(self, method):
            self._client = _Client(method)

        def detail(self, client : Client):
            return self._client._detail(client=client)
        

    class _Create_Expense:
        def __init__(self, method):
            self._expense = _Expense(method)

        def detail(self, expense : Expense):
            return self._expense._detail(expense=expense)


    class _Create_Invoice:
        def __init__(self, method):
            self._invoice = _Invoice(method)

        def create(self, project_id : str, calculator_id : str):
            return self._invoice._create(project_id=project_id, calculator_id=calculator_id)
    

    class _Create_Project:
        def __init__(self, method):
            self._project = _Project(method)

        def detail(self, project : Project):
            return self._project._detail(project=project)
        
        def contact(self, contact : Contact):
            return self._project._contact(contact=contact)


    class _Create_Staff:
        def __init__(self, method):
            self._staff = _Staff(method)
        
        def detail(self, staff : User):
            return self._staff._detail(staff=staff)


    class _Create_Task:
        def __init__(self, method):
            self._task = _Task(method)

        def detail(self, task : Task):
            return self._task._detail(task=task)


    class _Create_Time:
        def __init__(self, method):
            self._time = _Time(method)

        def __call__(self, time : Time, mark_submitted : bool = False):
            return self._time(time=time, mark_submitted=mark_submitted)