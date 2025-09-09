from api_wrapper.models import Result, Payment

class _Payment:
    def __init__(self, method):
        self._endpoint = "Payment"
        self._method = method

    def __call__(self, show_inactive : bool = False) -> list[Payment]:
        params = {}
        if show_inactive:
            params["show_inactive"] = "true"
        result: Result = self._method(endpoint=f"{self._endpoint}", params=params)
        return [Payment(**payment) for payment in result.data]

    def _detail(self, payment_id : str = None, view : str = None, show_all_contacts : bool = False, payment : Payment = None) -> Payment | Result:
        params = {}
        if view:
            params["view"] = view
        if show_all_contacts:
            params["showallcontacts"] = "true"
        if payment:
            params = {**payment}
        result: Result = self._method(endpoint=f"{self._endpoint}/Detail/{payment_id}" if payment_id else f"{self._endpoint}/Detail", params=params)
        return Payment(**result.data) if result.data else f"{result.status_code}: {result.message}"