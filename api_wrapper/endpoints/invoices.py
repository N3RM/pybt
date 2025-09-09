from api_wrapper.models import Result, Invoice

class _Invoice:
    def __init__(self, method):
        self._endpoint = "Invoice"
        self._method = method

    def __call__(self, show_inactive : bool = False) -> list[Invoice]:
        params = {}
        if show_inactive:
            params["show_inactive"] = "true"
        result: Result = self._method(endpoint=f"{self._endpoint}", params=params)
        return [Invoice(**invoice) for invoice in result.data]

    def _detail(self, invoice_id : str = None, view : str = None, show_all_contacts : bool = False, invoice : Invoice = None) -> Invoice | Result:
        params = {}
        if view:
            params["view"] = view
        if show_all_contacts:
            params["showallcontacts"] = "true"
        if invoice:
            params = {**invoice}
        result: Result = self._method(endpoint=f"{self._endpoint}/Detail/{invoice_id}" if invoice_id else f"{self._endpoint}/Detail", params=params)
        return Invoice(**result.data) if result.data else f"{result.status_code}: {result.message}"