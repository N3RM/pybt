from api_wrapper.models import Result

class PicklistEndPoint:
    def __init__(self, method: callable) -> None:
        self.method = method

    def _projects(self, endpoint: str, params: dict, data: dict):
        result: Result = self.method(
            endpoint=endpoint,
            params=params,
            data=data,
        )
        return result.data