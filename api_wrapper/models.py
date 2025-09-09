from datetime import date

class Base:
    def __repr__(self):
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
        self.id: str = Sid
        self.name: str = Name
        self.value: str = Value


class CustomFields(Base):
    def __init__(
            self,
            field_list: list[CustomField]
    ):
        self.field_list = field_list


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
        self.address = Address
        self.city = City
        self.state = State
        self.zip = Zip
        self.country = Country


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
        self.tag = Tag
        self.project_id = ProjectSid
        self.client_id = ClientSid
        self.first_name = FName
        self.last_name = SName
        self.company_name = CompanyNm
        self.email = Email
        self.address = Address


class Client(Base):
    def __init__(
        self,
        SystemId: str = None,
        Nm: str = None,
        **kwargs
    ):
        self.id = SystemId
        self.name = Nm


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
        self.id = SystemId
        self.name = Nm
        self.project_code = ProjectCode
        self.type_id = TypeId
        self.start_date = date.fromisoformat(StartDt) if StartDt else StartDt
        self.end_date = date.fromisoformat(EndDt) if EndDt else EndDt
        self.production_status = StatusProd
        self.production_status_id = StatusProd_nt
        self.billing_status = StatusBill
        self.notes = Notes
        self.is_all_staff = True if IsAllStaff == "true" else False
        self.is_no_charge = True if IsNoCharge == "true" else False
        self.invoice_type = InvoiceType
        self.invoice_totals = InvoiceTotals
        self.contract_notes = ContractNotes
        self.invoice_notes = InvoiceNotes
        self.billing_rate = BillingRate
        self.basic_rate = float(BasicRate)
        self.qb_customer_id = QBCustomerId
        self.client_id = ClientId
        self.billing_contact_id = BillingContactId
        self.contact_list = ContactList
        self.address_list = AddressList
        self.client = Client


class ProjectCustomField(CustomField):
    def __init__(
        self,
        ProjectSid: str = None,
        Sid: str = None,
        Name: str = None,
        Value: str = None,
        **kwargs
    ):
        super().__init__(Sid, Name, Value)
        self.project_id = ProjectSid


class TaskAssignment(Base):
    def __init__(
        self,
        StaffSid: str = None,
        Nm: str = None,
        **kwargs
    ):
        self.staff_id = StaffSid
        self.name = Nm


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
        self.id = TaskSid
        self.project_id = ProjectSid
        self.name = TaskNm
        self.group = TaskGroup
        self.full_name = FullName
        self.type_id = TaskType
        self.type = TaskType_nm
        self.current_status = CurrentStatus
        self.task_id = TaskId
        self.priority = Priority
        self.notes = Notes
        self.number_staff_assigned = AssignCount
        self.staff_assigned = AssignmentList
        self.due_date = DueDt
        self.start_date = StartDt
        self.fee_or_expense = FeeOrExpense
        self.budget_hours = BudgetHours
        self.budget_fees = BudgetFees
        self.budget_expenses = BudgetExps
        self.budget_total = BudgetTotal
        self.percent_complete = PerComp
        self.is_archived = IsArchived
        self.default_qb_class = DefaultQBClass
        self.is_series_master = IsSeriesMaster
        self.master_task_id = MasterTaskSid
        self.parent_id = ParentSid
        self.no_charge = NoCharge


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
        self.task_id = TaskSid
        self.input_hours = HoursInput
        self.billable_hours = HoursBill
        self.billable_fees = FeesInput
        self.input_cost = FeesCost
        self.input_expenses = ExpensesInput
        self.billable_expenses = ExpensesBillable
        self.total_work_in_progress = TotalWip


class ProjectBudget(Base):
    def __init__(
        self,
        ProjectSid: str = None,
        TaskBudgets: list[TaskBudgetData] = None,
        **kwargs
    ):
        self.project_id = ProjectSid
        self.task_budgets = TaskBudgets


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
        self.line_number = LineNbr
        self.name = Nm
        self.nt = Nt # TODO Figure out what this is
        self.account_id = AcctSid # TODO Figure out what this is
        self.budget_percent = BudgetPer # TODO Figure out what this is
        self.is_credit = IsCredit
        self.is_non_time_charge = IsNonTimeCharge
        self.is_taxable = IsTaxable
        self.qb_class_id = QBClassSid
        self.quantity = Quantity
        self.rate = Rate
        self.amount = Amt
        self.sales_tax_id = SalesTaxSid
        self.subtotal_id = SubTotalSid
        self.updated_line_number = UpdatedLineNbr
        self.is_deleted = IsDeleted
        self.account_name = AcctSidNm
        self.invoice_id = InvoiceSid
        self.type = LineType # TODO Figure out what this is
        self.project_id = ProjectSid
        self.qb_class_name = QBClassNm
        self.sales_tax_amount = SalesTaxAmt
        self.sales_tax_name = SalesTaxNm
        self.source = Source # TODO Figure out what this is


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
        self.id = Sid
        self.client_id = ClientSid
        self.project_id = ProjectSid
        self.client_name = ClientNm
        self.display_name = DName
        self.billing_contact_id = BillingContactId
        self.calculator = Calculator
        self.can_edit_invoice = CanEditInvoice
        self.invoice_number = InvoiceNbr
        self.invoice_date = InvoiceDt
        self.invoice_amount = InvoiceAmt
        self.subtotal = Subtotal
        self.total_amount = TotalAmt
        self.paid_amount = PaidAmt
        self.sales_tax_amount = SalesTaxAmt
        self.start_date = InvoiceDtSt
        self.end_date = InvoiceDtEnd
        self.sent_date = InvoiceDtSent
        self.note_1 = Note1
        self.note_2 = Note2
        self.purchase_order_number = PONumber
        self.status_id = Status
        self.status = StatusTxt
        self.accounts_receivable_id = ARAcctSid
        self.sales_tax_id = SalesTaxSid
        self.terms_id = TermsSid
        self.due_date = InvoiceDtDue
        self.posted_status = PostedStatus
        self.billing_address = BillingAddress
        self.firm_address = FirmAddress
        self.lines = Lines


class Report(Base):
    def __init__(
        self,
        Data = None,
        FieldList = None,
        **kwargs
    ):
        self.data = Data
        self.field_list = FieldList


class User(Base):
    def __init__(
        self,
        StaffSid: str = None,
        FName: str = None,
        SName: str = None,
        Email: str = None,
        **kwargs
    ):
        self.id = StaffSid
        self.first_name = FName
        self.last_name = SName
        self.email = Email


class Rate(Base):
    def __init__(
        self,
        ProjectSid: str = None,
        RateValue: str = None,
        StaffSid = None,
        TaskSid = None,
        **kwargs
    ):
        self.project_id = ProjectSid
        self.staff_id = StaffSid
        self.task_id = TaskSid
        self.value = RateValue


class ProjectTeamMember(Base):
    def __init__(
        self,
        StaffSid: str = None,
        ContactRole: str = None,
        TeamLead: bool = False,
        **kwargs
    ):
        self.staff_id = StaffSid
        self.role = ContactRole
        self.team_lead = TeamLead


class ProjectTeam(Base):
    def __init__(
            self,
            team_members: list[ProjectTeamMember],
            project_id: str,
    ):
        self.team_members = team_members
        self.project_id = project_id


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
        self.id = Sid
        self.is_submitted = IsSubmitted
        self.report_id = RptSid
        self.staff_id = StaffSid
        self.date = Dt
        self.project_id = ProjectSid
        self.project = ProjectNm
        self.client_id = ClientId
        self.client = ClientNm
        self.category_id = CatSid
        self.category = CatNm
        self.task_id = TaskSid
        self.task = TaskNm
        self.vendor_id = VendorSid
        self.vendor = VendorNm
        self.credit_card_id = CCardSid
        self.bill_id = BillSid
        self.no_charge = NoCharge
        self.paid_by_company = PaidByCo
        self.notes = Nt
        self.input_amount = CostIn
        self.reimbursable_amount = CostPayable
        self.billable_amount = CostBill
        self.is_unit = IsUnit
        self.unit_price = UnitPrice
        self.unit_rate = UnitRate
        self.units = Units
        self.unit_of_measure = UOM
        self.due_date = DueDate
        self.reference_number = RefNbr
        self.has_receipt = HasReceipt
        self.is_approved = IsApproved
        self.approval_status_id = ApprovalStatus
        self.approval_status = ApprovalStatusNm
        self.invoice_id = InvoiceSid
        self.is_invoiced = IsInvoiced
        self.is_vendor_expense = IsVenderExpense
        self.expense_receipt = ExpenseReceipt


class ExpenseReport(Base):
    def __init__(
        self,
        Sid: str = None,
        RptNm: str = None,
        CreatedDt: str = None,
        StatusId: str = None,
        **kwargs
    ):
        self.id = Sid
        self.report_name = RptNm
        self.date_created = CreatedDt
        self.status_id = StatusId


class Picklist(Base):
    def __init__(
        self,
        result: list,
        **kwargs
    ):
        self.result = result

    def __repr__(self):
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


class PicklistProject(PicklistIdName):
    def __init__(
        self,
        Id: str = None,
        Name: str = None,
        Group: str = None,
        **kwargs
    ):
        super().__init__(Id, Name, **kwargs)
        self.group = Group

class PicklistClient(PicklistIdName):
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
        self.id = SID
        self.is_new = IsNew
        self.date = Dt
        self.project_id = ProjectSID
        self.project = ProjectNm
        self.client_id = ClientId
        self.client = ClientNm
        self.staff_id = StaffSID
        self.staff = SourceNm
        self.task_id = TaskSID
        self.task = TaskNm
        self.input_hours = Hours_IN
        self.notes = Notes
        self.revision_notes = RevisionNotes
        self.no_charge = NoCharge
        self.is_approved = IsApproved
        self.invoice_id = InvoiceSID
        self.is_invoiced = IsInvoiced
        self.billable_hours = HoursBillable
        self.billing_rate = BillRate
        self.billable_charges = ChargeBillable


class Timesheet(Base):
    def __init__(
        self,
        start_date: str = None,
        end_date: str = None,
        time_entries: list[Time] = None,
        **kwargs
    ):
        self.start_date = start_date
        self.end_date = end_date
        self.time_entries = time_entries

    def __repr__(self):
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


class ProjectTimesheet(Base):
    def __init__(
        self,
        projectSID: str = None,
        timesheet: Timesheet = None,
        **kwargs
    ):
        self.timesheet = timesheet
        self.project_id = projectSID


class StaffTimesheet(Base):
    def __init__(
        self,
        staffSID: str = None,
        timesheet: Timesheet = None,
        **kwargs
    ):
        self.timesheet = timesheet
        self.staff_id = staffSID


class Ticket: ...