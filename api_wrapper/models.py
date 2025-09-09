from datetime import date

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
    def __init__(
        self,
        status_code: int,
        message: str = "",
        data = None
    ):
        self.status_code = str(status_code)
        self.message = str(message)
        self.data = data if data else None

    def __repr__(self):
        return f"{self.status_code}: {self.message}"


class CustomField(Base):
    def __init__(
        self,
        Sid: str = None,
        Name: str = None,
        Value: str = None,
        **kwargs
    ):
        self.Sid: str = Sid
        self.Name: str = Name
        self.Value: str = Value


class Address(Base):
    def __init__(
        self,
        Address: str = None,
        City: str = None,
        State: str = None,
        Zip: str = None,
        Country: str = None,
        **kwargs
    ):
        self.Address = Address
        self.City = City
        self.State = State
        self.Zip = Zip
        self.Country = Country


class Contact(Base):
    def __init__(
        self,
        id: str = None,
        Tag: str = None,
        ProjectSid: str = None,
        ClientSid: str = None,
        FName: str = None,
        SName: str = None,
        CompanyNm: str = None,
        Email: str = None,
        Address: Address = None,
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
    def __init__(
        self,
        SystemId: str = None,
        Nm: str = None,
        ClientId: str = None,
        **kwargs
    ):
        self.SystemId = SystemId
        self.Nm = Nm
        self.ClientId = ClientId


class Project(Base):
    def __init__(
        self,
        SystemId: str = None,
        Nm: str = None,
        ProjectCode: str = None,
        TypeId: str = None,
        StartDt: str = None,
        EndDt: str = None,
        StatusProd: str = None,
        StatusProd_nt: str = None,
        StatusBill: str = None,
        Notes: str = None,
        IsAllStaff: bool = None,
        IsNoCharge: bool = None,
        InvoiceType: str = None,
        InvoiceTotals: str = None,
        ContractNotes: str = None,
        InvoiceNotes: str = None,
        BillingRate: str = None,
        BasicRate: str = None,
        QBCustomerId: str = None,
        ClientId: str = None,
        BillingContactId: str = None,
        ContactList: list[Contact] = None,
        AddressList: list[Address] = None,
        Client: Client = None,
        **kwargs,
    ):
        self.SystemId = SystemId
        self.Nm = Nm
        self.ProjectCode = ProjectCode
        self.TypeId = TypeId
        self.StartDt = date.fromisoformat(StartDt) if StartDt else StartDt
        self.EndDt = date.fromisoformat(EndDt) if EndDt else EndDt
        self.StatusProd = StatusProd
        self.StatusProd_nt = StatusProd_nt
        self.StatusBill = StatusBill
        self.Notes = Notes
        self.IsAllStaff = True if IsAllStaff == "true" else False
        self.IsNoCharge = True if IsNoCharge == "true" else False
        self.InvoiceType = InvoiceType
        self.InvoiceTotals = InvoiceTotals
        self.ContractNotes = ContractNotes
        self.InvoiceNotes = InvoiceNotes
        self.BillingRate = BillingRate
        self.BasicRate = float(BasicRate)
        self.QBCustomerId = QBCustomerId
        self.ClientId = ClientId
        self.BillingContactId = BillingContactId
        self.ContactList = ContactList
        self.AddressList = AddressList
        self.Client = Client


class ProjectCustomField(CustomField, Base):
    def __init__(
        self,
        ProjectSid: str = None,
        Sid: str = None,
        Name: str = None,
        Value: str = None,
        **kwargs
    ):
        super().__init__(Sid, Name, Value)
        self.project_sid = ProjectSid


class TaskAssignment(Base):
    def __init__(
        self,
        StaffSid: str = None,
        Nm: str = None,
        **kwargs
    ):
        self.StaffSid = StaffSid
        self.Nm = Nm


class Task(Base):
    def __init__(
        self,
        TaskSid: str = None,
        ProjectSid: str = None,
        TaskNm: str = None,
        TaskGroup: str = None,
        FullName: str = None,
        TaskType: str = None,
        TaskType_nm: str = None,
        CurrentStatus: str = None,
        TaskId: str = None,
        Priority: str = None,
        Notes: str = None,
        AssignCount: str = None,
        AssignmentList: list[TaskAssignment] = None,
        DueDt: str = None,
        StartDt: str = None,
        FeeOrExpense: str = None,
        BudgetHours: str = None,
        BudgetFees: str = None,
        BudgetExps: str = None,
        BudgetTotal: str = None,
        PerComp: str = None,
        IsArchived: bool = None,
        DefaultQBClass: str = None,
        IsSeriesMaster: bool = None,
        MasterTaskSid: str = None,
        ParentSid: str = None,
        NoCharge: bool = None, 
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
        TaskSid: str = None,
        HoursInput: str = None,
        HoursBill: str = None,
        FeesInput: str = None,
        FeesCost: str = None,
        ExpensesInput: str = None,
        ExpensesBillable: str = None,
        TotalWip: str = None, **kwargs
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
    def __init__(
        self,
        ProjectSid: str = None,
        TaskBudgets: list[TaskBudgetData] = None,
        **kwargs
    ):
        self.ProjectSid = ProjectSid
        self.TaskBudgets = TaskBudgets


class LineItem(Base):
    def __init__(
        self,
        LineNbr: str = None,
        Nm: str = None,
        Nt: str = None,
        AcctSid: str = None,
        BudgetPer: str = None,
        IsCredit: bool = None,
        IsNonTimeCharge: bool = None,
        IsTaxable: bool = None,
        QBClassSid: str = None,
        Quantity: str = None,
        Rate: str = None,
        Amt: str = None,
        SalesTaxSid: str = None,
        SubTotalSid: str = None,
        UpdatedLineNbr: str = None,
        IsDeleted: bool = None,
        AcctSidNm: str = None,
        InvoiceSid: str = None,
        LineType: str = None,
        ProjectSid: str = None,
        QBClassNm: str = None,
        SalesTaxAmt: str = None,
        SalesTaxNm: str = None,
        Source: str = None, **kwargs
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
        Sid: str = None,
        ClientSid: str = None,
        ProjectSid: str = None,
        ClientNm: str = None,
        DName: str = None,
        BillingContactId: str = None,
        Calculator: str = None,
        CanEditInvoice: bool = None,
        InvoiceNbr: str = None,
        InvoiceDt: str = None,
        InvoiceAmt: str = None,
        Subtotal: str = None,
        TotalAmt: str = None,
        PaidAmt: str = None,
        SalesTaxAmt: str = None,
        InvoiceDtSt: str = None,
        InvoiceDtEnd: str = None,
        InvoiceDtSent: str = None,
        Note1: str = None,
        Note2: str = None,
        PONumber: str = None,
        Status: str = None,
        StatusTxt: str = None,
        ARAcctSid: str = None,
        SalesTaxSid: str = None,
        TermsSid: str = None,
        InvoiceDtDue: str = None,
        PostedStatus: str = None,
        BillingAddress: Address = None,
        FirmAddress: Address = None,
        Lines: list[LineItem] = None,
        **kwargs
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
    def __init__(
        self,
        Data = None,
        FieldList = None,
        **kwargs
    ):
        self.Data = Data
        self.FieldList = FieldList


class User(Base):
    def __init__(
        self,
        StaffSid: str = None,
        FName: str = None,
        SName: str = None,
        Email: str = None,
        **kwargs
    ):
        self.StaffSid = StaffSid
        self.FName = FName
        self.SName = SName
        self.Email = Email


class Rate(Base):
    def __init__(
        self,
        ProjectSid: str = None,
        RateValue: str = None,
        StaffSid = None,
        TaskSid = None,
        **kwargs
    ):
        self.ProjectSid = ProjectSid
        self.StaffSid = StaffSid
        self.TaskSid = TaskSid
        self.RateValue = RateValue


class ProjectTeamMember(Base):
    def __init__(
        self,
        StaffSid: str = None,
        ContactRole: str = None,
        TeamLead: bool = False,
        **kwargs
    ):
        self.StaffSid = StaffSid
        self.ContactRole = ContactRole
        self.TeamLead = TeamLead


class Expense(Base):
    def __init__(
        self,
        Sid: str = None,
        IsSubmitted: bool = None,
        RptSid: str = None,
        StaffSid: str = None,
        Dt: str = None,
        ProjectSid: str = None,
        ProjectNm: str = None,
        ClientId: str = None,
        ClientNm: str = None,
        CatSid: str = None,
        CatNm: str = None,
        TaskSid: str = None,
        TaskNm: str = None,
        VendorSid: str = None,
        VendorNm: str = None,
        CCardSid: str = None,
        BillSid: str = None,
        NoCharge: bool = None,
        PaidByCo: bool = None,
        Nt: str = None,
        CostIn: str = None,
        CostPayable: str = None,
        CostBill: str = None,
        IsUnit: bool = None,
        UnitPrice: str = None,
        UnitRate: str = None,
        Units: str = None,
        UOM: str = None,
        DueDate: str = None,
        RefNbr: str = None,
        HasReceipt: bool = None,
        IsApproved: bool = None,
        ApprovalStatus: str = None,
        ApprovalStatusNm: str = None,
        InvoiceSid: str = None,
        IsInvoiced: bool = None,
        IsVenderExpense: bool = None,
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
    def __init__(
        self,
        Sid: str = None,
        RptNm: str = None,
        CreatedDt: str = None,
        StatusId: str = None,
        **kwargs
    ):
        self.Sid = Sid
        self.RptNm = RptNm
        self.CreatedDt = CreatedDt
        self.StatusId = StatusId


class Picklist(Base):
    def __init__(
        self,
        result: list,
        **kwargs
    ):
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
    def __init__(
        self,
        Id: str = None,
        Name: str = None,
        **kwargs
    ):
        self.id = Id
        self.name = Name


class PicklistProject(PicklistIdName, Base):
    def __init__(
        self,
        Id: str = None,
        Name: str = None,
        Group: str = None,
        **kwargs
    ):
        super().__init__(Id, Name, **kwargs)
        self.group = Group

class PicklistClient(PicklistIdName, Base):
    def __init__(
        self,
        Id : str = None,
        Name : str = None,
        **kwargs
    ):
        super().__init__(Id, Name, **kwargs)


class Time(Base):
    def __init__(
        self,
        SID: str = None,
        Dt: str = None,
        ProjectSID: str = None,
        StaffSID: str = None,
        TaskSID: str = None,
        Hours_IN: str = None,
        Notes: str = None,
        HoursBillable: str = None,
        ChargeBillable: str = None,
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
    def __init__(
        self,
        start_date: str = None,
        end_date: str = None,
        timesheet = None,
        **kwargs
    ):
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
        projectSID: str = None,
        start_date: str = None,
        end_date: str = None,
        timesheet = None, **kwargs
    ):
        super().__init__(start_date, end_date, timesheet)
        self.projectSID = projectSID


class StaffTimesheet(Timesheet):
    def __init__(
        self,
        staffSID: str = None,
        start_date: str = None,
        end_date: str = None,
        timesheet = None, **kwargs
    ):
        super().__init__(start_date, end_date, timesheet)
        self.staffSID = staffSID


class Ticket: ...