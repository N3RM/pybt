from datetime import date

from api_wrapper.models import Result, Invoice
from api_wrapper.utils import format_bigtime_date

class _Invoice:
    def __init__(self, method):
        self._endpoint = "Invoice"
        self._method = method

    def _detail(self, invoice_id : str = None, invoice : Invoice = None) -> Invoice | Result:
        params = {}
        if invoice:
            params = {**invoice}
        result: Result = self._method(endpoint=f"{self._endpoint}/Detail/{invoice_id}" if invoice_id else f"{self._endpoint}/Detail", params=params)
        return Invoice(**result.data) if result.data else f"{result.status_code}: {result.message}"
    
    def _create(self, project_id : str, calculator_id : str):
        params = {}
        params["projectsid"] = project_id
        params["invoicetype"] = calculator_id

        result: Result = self._method(endpoint=f"{self._endpoint}/Create", params=params)
        return Invoice(**result.data)
    
    def _history(self, start_date : date, end_date : date) -> list[Invoice]:
        params = {}
        params["startdt"] = format_bigtime_date(start_date)
        params["enddt"] = format_bigtime_date(end_date)

        result: Result = self._method(endpoint=f"{self._endpoint}/History", params=params)
        return [Invoice(**invoice) for invoice in result.data]
    
    def _drafts(self, start_date : date = None, end_date : date = None) -> list[Invoice]:
        params = {}
        if start_date:
            params["startdt"] = format_bigtime_date(start_date)
        if end_date:
            params["enddt"] = format_bigtime_date(end_date)

        result: Result = self._method(endpoint=f"{self._endpoint}/History", params=params)
        return [Invoice(**invoice) for invoice in result.data]
    
    def _invoices_by_client(self, client_id : str, start_date : date, end_date : date):
        params = {}
        params["clientid"] = client_id
        params["startdt"] = format_bigtime_date(start_date)
        params["enddt"] = format_bigtime_date(end_date)

        result: Result = self._method(endpoint=f"{self._endpoint}/GetInvoicesByClientId", params=params)
        return [Invoice(**invoice) for invoice in result.data]