from enum import Enum
from datetime import date

import calendar

def get_month_start_date(month : int, year : int) -> date:
    return date(year, month, 1)

def get_month_end_date(month : int = None, year : int = None) -> date:
    return date(year, month, 1).replace(
        day=calendar.monthrange(year, month)[1]
    )

def get_this_month_start_date() -> date:
    return get_month_start_date(month=date.today().month, year=date.today().year)

def get_this_month_end_date() -> date:
    return get_month_end_date(month=date.today().month, year=date.today().year)

def get_last_month_start_date() -> date:
    month = date.today().month
    year = date.today().year
    last_month = month - 1
    if last_month == 0:
        last_month = 12
        year -= 1

    return get_month_start_date(month=last_month, year=year)

def get_last_month_end_date() -> date:
    month = date.today().month
    year = date.today().year
    last_month = month - 1
    if last_month == 0:
        last_month = 12
        year -= 1

    return get_month_end_date(month=last_month, year=year)

def format_bigtime_date(dt: date) -> str:
    return dt.strftime("%Y-%m-%d")


class PicklistFieldValueChoices(Enum):
    INVOICE_TYPE_SUBTOTAL = "InvoiceType_subttl"
    RATE_TYPE_SIMPLE = "rateTypeSimple"
    LOOKUP_STAFF_HOURLY_TYPE = "LookupStaffHourlyType"
    LOOKUP_STAFF_TYPE = "LookupStaffType"
    LOOKUP_CLIENT_TYPE = "LookupClientType"
    LOOKUP_PROJECT_TYPE = "LookupProjectType"
    LOOKUP_PROJECT_TEAM_ROLES = "LookupProjectTeamRoles"
    LOOKUP_CONTACT_TYPE = "LookupContactType"
    STAFF_ORG_LIST = "StaffOrgList"
    STAFF_TEAM_LIST = "StaffTeamList"
    CURRENCY_LIST = "CurrencyList"
    SECURITY_GROUPS = "SecurityGroups"
    PRODUCTION_STATUS = "StatusProduction"
    BILLING_STATUS = "StatusBilling"
    STAFF_STATUS = "StatusStaff"
    EXPENSE_REPORT_STATUS = "StatusExpenseRpt"
    INVOICE_TYPES = "InvoiceTypes"
    INVOICE_POST_TYPES = "InvoicePostTypes"


class ViewChoices(Enum):
    BASIC = "Basic"
    DETAILED = "Detailed"