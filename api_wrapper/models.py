from typing import List, Dict


class Base:
    def __str__(self):
        return str(
            {
                key: value
                for key, value in self.__dict__.items()
                if not key.startswith("__")
                and not callable(value)
                and not callable(getattr(value, "__get__", None))
            }
        )


class Result(Base):
    def __init__(self, status_code: int, message: str = "", data = None):
        self.status_code = str(status_code)
        self.message = str(message)
        self.data = data if data else []


class CustomField(Base):
    def __init__(self, Sid: str, Name: str, Value: str, **kwargs):
        self.Sid: str = Sid
        self.Name: str = Name
        self.Value: str = Value


class Address(Base):
    def __init__(
        self, Address: str, City: str, State: str, Zip: str, Country: str, **kwargs
    ):
        self.Address = Address
        self.City = City
        self.State = State
        self.Zip = Zip
        self.Country = Country


class Contact(Base):
    def __init__(
        self,
        id: str,
        Tag: str,
        ProjectSid: str,
        ClientSid: str,
        FName: str,
        SName: str,
        CompanyNm: str,
        Email: str,
        Address: Address,
        **kwargs,
    ):
        self.id = id
        self.Tag = Tag
        self.ProjectSid = ProjectSid
        self.ClientSid = ClientSid
        self.FName = FName
        self.SName = SName
        self.CompanyNm = CompanyNm
        self.Email = Email
        self.Address = Address


class Client(Base):
    def __init__(self, SystemId: str, Nm: str, ClientId: str, **kwargs):
        self.SystemId = SystemId
        self.Nm = Nm
        self.ClientId = ClientId


class Project(Base):
    def __init__(
        self,
        SystemId: str,
        Nm: str,
        ProjectCode: str,
        TypeId: str,
        StartDt: str,
        EndDt: str,
        StatusProd: str,
        StatusProd_nt: str,
        StatusBill: str,
        Notes: str,
        IsAllStaff: bool,
        IsNoCharge: bool,
        InvoiceType: str,
        InvoiceTotals: str,
        ContractNotes: str,
        InvoiceNotes: str,
        BillingRate: str,
        BasicRate: str,
        QBCustomerId: str,
        ClientId: str,
        BillingContactId: str,
        ContactList: List[Contact],
        AddressList: List[Address],
        Client: Client,
        **kwargs,
    ):
        self.SystemId = SystemId
        self.Nm = Nm
        self.ProjectCode = ProjectCode
        self.TypeId = TypeId
        self.StartDt = StartDt
        self.EndDt = EndDt
        self.StatusProd = StatusProd
        self.StatusProd_nt = StatusProd_nt
        self.StatusBill = StatusBill
        self.Notes = Notes
        self.IsAllStaff = IsAllStaff
        self.IsNoCharge = IsNoCharge
        self.InvoiceType = InvoiceType
        self.InvoiceTotals = InvoiceTotals
        self.ContractNotes = ContractNotes
        self.InvoiceNotes = InvoiceNotes
        self.BillingRate = BillingRate
        self.BasicRate = BasicRate
        self.QBCustomerId = QBCustomerId
        self.ClientId = ClientId
        self.BillingContactId = BillingContactId
        self.ContactList = ContactList
        self.AddressList = AddressList
        self.Client = Client


class ProjectCustomField(CustomField, Base):
    def __init__(self, ProjectSid: str, Sid: str, Name: str, Value: str, **kwargs):
        super().__init__(Sid, Name, Value)
        self.project_sid = ProjectSid


class TaskAssignment(Base):
    def __init__(self, StaffSid: str, Nm: str, **kwargs):
        self.StaffSid = StaffSid
        self.Nm = Nm


class Task(Base):
    def __init__(
        self,
        TaskSid: str,
        ProjectSid: str,
        TaskNm: str,
        TaskGroup: str,
        FullName: str,
        TaskType: str,
        TaskType_nm: str,
        CurrentStatus: str,
        TaskId: str,
        Priority: str,
        Notes: str,
        AssignCount: str,
        AssignmentList: List[TaskAssignment],
        DueDt: str,
        StartDt: str,
        FeeOrExpense: str,
        BudgetHours: str,
        BudgetFees: str,
        BudgetExps: str,
        BudgetTotal: str,
        PerComp: str,
        IsArchived: bool,
        DefaultQBClass: str,
        IsSeriesMaster: bool,
        MasterTaskSid: str,
        ParentSid: str,
        NoCharge: bool, 
        **kwargs
    ):
        self.TaskSid = TaskSid
        self.ProjectSid = ProjectSid
        self.TaskNm = TaskNm
        self.TaskGroup = TaskGroup
        self.FullName = FullName
        self.TaskType = TaskType
        self.TaskType_nm = TaskType_nm
        self.CurrentStatus = CurrentStatus
        self.TaskId = TaskId
        self.Priority = Priority
        self.Notes = Notes
        self.AssignCount = AssignCount
        self.AssignmentList = AssignmentList
        self.DueDt = DueDt
        self.StartDt = StartDt
        self.FeeOrExpense = FeeOrExpense
        self.BudgetHours = BudgetHours
        self.BudgetFees = BudgetFees
        self.BudgetExps = BudgetExps
        self.BudgetTotal = BudgetTotal
        self.PerComp = PerComp
        self.IsArchived = IsArchived
        self.DefaultQBClass = DefaultQBClass
        self.IsSeriesMaster = IsSeriesMaster
        self.MasterTaskSid = MasterTaskSid
        self.ParentSid = ParentSid
        self.NoCharge = NoCharge


class TaskBudgetData(Base):
    def __init__(
        self,
        TaskSid: str,
        HoursInput: str,
        HoursBill: str,
        FeesInput: str,
        FeesCost: str,
        ExpensesInput: str,
        ExpensesBillable: str,
        TotalWip: str, **kwargs
    ):
        self.TaskSid = TaskSid
        self.HoursInput = HoursInput
        self.HoursBill = HoursBill
        self.FeesInput = FeesInput
        self.FeesCost = FeesCost
        self.ExpensesInput = ExpensesInput
        self.ExpensesBillable = ExpensesBillable
        self.TotalWip = TotalWip


class ProjectBudget(Base):
    def __init__(self, ProjectSid: str, TaskBudgets: List[TaskBudgetData], **kwargs):
        self.ProjectSid = ProjectSid
        self.TaskBudgets = TaskBudgets


class LineItem(Base):
    def __init__(
        self,
        LineNbr: str,
        Nm: str,
        Nt: str,
        AcctSid: str,
        BudgetPer: str,
        IsCredit: bool,
        IsNonTimeCharge: bool,
        IsTaxable: bool,
        QBClassSid: str,
        Quantity: str,
        Rate: str,
        Amt: str,
        SalesTaxSid: str,
        SubTotalSid: str,
        UpdatedLineNbr: str,
        IsDeleted: bool,
        AcctSidNm: str,
        InvoiceSid: str,
        LineType: str,
        ProjectSid: str,
        QBClassNm: str,
        SalesTaxAmt: str,
        SalesTaxNm: str,
        Source: str, **kwargs
    ):
        self.LineNbr = LineNbr
        self.Nm = Nm
        self.Nt = Nt
        self.AcctSid = AcctSid
        self.BudgetPer = BudgetPer
        self.IsCredit = IsCredit
        self.IsNonTimeCharge = IsNonTimeCharge
        self.IsTaxable = IsTaxable
        self.QBClassSid = QBClassSid
        self.Quantity = Quantity
        self.Rate = Rate
        self.Amt = Amt
        self.SalesTaxSid = SalesTaxSid
        self.SubTotalSid = SubTotalSid
        self.UpdatedLineNbr = UpdatedLineNbr
        self.IsDeleted = IsDeleted
        self.AcctSidNm = AcctSidNm
        self.InvoiceSid = InvoiceSid
        self.LineType = LineType
        self.ProjectSid = ProjectSid
        self.QBClassNm = QBClassNm
        self.SalesTaxAmt = SalesTaxAmt
        self.SalesTaxNm = SalesTaxNm
        self.Source = Source


class Invoice(Base):
    def __init__(
        self,
        Sid: str,
        ClientSid: str,
        ProjectSid: str,
        ClientNm: str,
        DName: str,
        BillingContactId: str,
        Calculator: str,
        CanEditInvoice: bool,
        InvoiceNbr: str,
        InvoiceDt: str,
        InvoiceAmt: str,
        Subtotal: str,
        TotalAmt: str,
        PaidAmt: str,
        SalesTaxAmt: str,
        InvoiceDtSt: str,
        InvoiceDtEnd: str,
        InvoiceDtSent: str,
        Note1: str,
        Note2: str,
        PONumber: str,
        Status: str,
        StatusTxt: str,
        ARAcctSid: str,
        SalesTaxSid: str,
        TermsSid: str,
        InvoiceDtDue: str,
        PostedStatus: str,
        BillingAddress: Address,
        FirmAddress: Address,
        Lines: List[LineItem], **kwargs
    ):
        self.Sid = Sid
        self.ClientSid = ClientSid
        self.ProjectSid = ProjectSid
        self.ClientNm = ClientNm
        self.DName = DName
        self.BillingContactId = BillingContactId
        self.Calculator = Calculator
        self.CanEditInvoice = CanEditInvoice
        self.InvoiceNbr = InvoiceNbr
        self.InvoiceDt = InvoiceDt
        self.InvoiceAmt = InvoiceAmt
        self.Subtotal = Subtotal
        self.TotalAmt = TotalAmt
        self.PaidAmt = PaidAmt
        self.SalesTaxAmt = SalesTaxAmt
        self.InvoiceDtSt = InvoiceDtSt
        self.InvoiceDtEnd = InvoiceDtEnd
        self.InvoiceDtSent = InvoiceDtSent
        self.Note1 = Note1
        self.Note2 = Note2
        self.PONumber = PONumber
        self.Status = Status
        self.StatusTxt = StatusTxt
        self.ARAcctSid = ARAcctSid
        self.SalesTaxSid = SalesTaxSid
        self.TermsSid = TermsSid
        self.InvoiceDtDue = InvoiceDtDue
        self.PostedStatus = PostedStatus
        self.BillingAddress = BillingAddress
        self.FirmAddress = FirmAddress
        self.Lines = Lines


class Report(Base):
    def __init__(self, Data, FieldList, **kwargs):
        self.Data = Data
        self.FieldList = FieldList


class User(Base):
    def __init__(self, StaffSid: str, FName: str, SName: str, Email: str, **kwargs):
        self.StaffSid = StaffSid
        self.FName = FName
        self.SName = SName
        self.Email = Email


class Rate(Base):
    def __init__(
        self, ProjectSid: str, RateValue: str, StaffSid = None, TaskSid = None, **kwargs
    ):
        self.ProjectSid = ProjectSid
        self.StaffSid = StaffSid
        self.TaskSid = TaskSid
        self.RateValue = RateValue


class ProjectTeamMember(Base):
    def __init__(self, StaffSid: str, ContactRole: str, TeamLead: bool = False, **kwargs):
        self.StaffSid = StaffSid
        self.ContactRole = ContactRole
        self.TeamLead = TeamLead


class Expense(Base):
    def __init__(
        self,
        Sid: str,
        IsSubmitted: bool,
        RptSid: str,
        StaffSid: str,
        Dt: str,
        ProjectSid: str,
        ProjectNm: str,
        ClientId: str,
        ClientNm: str,
        CatSid: str,
        CatNm: str,
        TaskSid: str,
        TaskNm: str,
        VendorSid: str,
        VendorNm: str,
        CCardSid: str,
        BillSid: str,
        NoCharge: bool,
        PaidByCo: bool,
        Nt: str,
        CostIn: str,
        CostPayable: str,
        CostBill: str,
        IsUnit: bool,
        UnitPrice: str,
        UnitRate: str,
        Units: str,
        UOM: str,
        DueDate: str,
        RefNbr: str,
        HasReceipt: bool,
        IsApproved: bool,
        ApprovalStatus: str,
        ApprovalStatusNm: str,
        InvoiceSid: str,
        IsInvoiced: bool,
        IsVenderExpense: bool,
        ExpenseReceipt = None, **kwargs
    ):
        self.Sid = Sid
        self.IsSubmitted = IsSubmitted
        self.RptSid = RptSid
        self.StaffSid = StaffSid
        self.Dt = Dt
        self.ProjectSid = ProjectSid
        self.ProjectNm = ProjectNm
        self.ClientId = ClientId
        self.ClientNm = ClientNm
        self.CatSid = CatSid
        self.CatNm = CatNm
        self.TaskSid = TaskSid
        self.TaskNm = TaskNm
        self.VendorSid = VendorSid
        self.VendorNm = VendorNm
        self.CCardSid = CCardSid
        self.BillSid = BillSid
        self.NoCharge = NoCharge
        self.PaidByCo = PaidByCo
        self.Nt = Nt
        self.CostIn = CostIn
        self.CostPayable = CostPayable
        self.CostBill = CostBill
        self.IsUnit = IsUnit
        self.UnitPrice = UnitPrice
        self.UnitRate = UnitRate
        self.Units = Units
        self.UOM = UOM
        self.DueDate = DueDate
        self.RefNbr = RefNbr
        self.HasReceipt = HasReceipt
        self.IsApproved = IsApproved
        self.ApprovalStatus = ApprovalStatus
        self.ApprovalStatusNm = ApprovalStatusNm
        self.InvoiceSid = InvoiceSid
        self.IsInvoiced = IsInvoiced
        self.IsVenderExpense = IsVenderExpense
        self.ExpenseReceipt = ExpenseReceipt


class ExpenseReport(Base):
    def __init__(self, Sid: str, RptNm: str, CreatedDt: str, StatusId: str, **kwargs):
        self.Sid = Sid
        self.RptNm = RptNm
        self.CreatedDt = CreatedDt
        self.StatusId = StatusId


class Picklist(Base):
    def __init__(self, result: list, **kwargs):
        self.result = result

    def __str__(self):
        datalist = []
        for data in self.result:
            datalist.append(
                {
                    key: value
                    for key, value in data.__dict__.items()
                    if not key.startswith("__")
                    and not callable(value)
                    and not callable(getattr(value, "__get__", None))
                }
            )
        return str(datalist)


class PicklistIdName(Base):
    def __init__(self, Id: str, Name: str, **kwargs):
        self.id = Id
        self.name = Name


class PicklistProject(PicklistIdName, Base):
    def __init__(self, Id: str, Name: str, Group: str, **kwargs):
        super().__init__(Id, Name, **kwargs)
        self.group = Group


class Time(Base):
    def __init__(
        self,
        SID: str,
        Dt: str,
        ProjectSID: str,
        StaffSID: str,
        TaskSID: str,
        Hours_IN: str,
        Notes: str,
        HoursBillable: str,
        ChargeBillable: str,
        IsNew = None,
        ProjectNm = None,
        ClientId = None,
        ClientNm = None,
        SourceNm = None,
        TaskNm = None,
        RevisionNotes = None,
        NoCharge = None,
        IsApproved = None,
        InvoiceSID = None,
        IsInvoiced = None,
        BillRate = None,
        **kwargs,
    ):
        self.SID = SID
        self.IsNew = IsNew
        self.Dt = Dt
        self.ProjectSID = ProjectSID
        self.ProjectNm = ProjectNm
        self.ClientId = ClientId
        self.ClientNm = ClientNm
        self.StaffSID = StaffSID
        self.SourceNm = SourceNm
        self.TaskSID = TaskSID
        self.TaskNm = TaskNm
        self.Hours_In = Hours_IN
        self.Notes = Notes
        self.RevisionNotes = RevisionNotes
        self.NoCharge = NoCharge
        self.IsApproved = IsApproved
        self.InvoiceSID = InvoiceSID
        self.IsInvoiced = IsInvoiced
        self.HoursBillable = HoursBillable
        self.BillRate = BillRate
        self.ChargeBillable = ChargeBillable


class Timesheet(Base):
    def __init__(self, start_date: str, end_date: str, timesheet = None, **kwargs):
        self.start_date = start_date
        self.end_date = end_date
        self.timesheet = timesheet

    def __str__(self):
        timelist = []
        for time in self.timesheet:
            timelist.append(
                {
                    key: value
                    for key, value in time.__dict__.items()
                    if not key.startswith("__")
                    and not callable(value)
                    and not callable(getattr(value, "__get__", None))
                }
            )
        return str(timelist)


class ProjectTimesheet(Timesheet):
    def __init__(
        self,
        projectSID: str,
        start_date: str,
        end_date: str,
        timesheet = None, **kwargs
    ):
        super().__init__(start_date, end_date, timesheet)
        self.projectSID = projectSID


class StaffTimesheet(Timesheet):
    def __init__(
        self,
        staffSID: str,
        start_date: str,
        end_date: str,
        timesheet = None, **kwargs
    ):
        super().__init__(start_date, end_date, timesheet)
        self.staffSID = staffSID
