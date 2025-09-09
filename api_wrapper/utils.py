from datetime import date
import calendar

def get_month_start_date() -> date:
        return date.today().replace(day=1)

def get_month_end_date() -> date:
    return date.today().replace(
        day=calendar.monthrange(date.today().year, date.today().month)[1]
    )

def format_bigtime_date(dt: date) -> str:
    return dt.strftime("%Y-%m-%d")