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
    
    def _clients(self, endpoint: str, params: dict, data: dict):
        result: Result = self.method(
            endpoint=endpoint,
            params=params,
            data=data,
        )
        return result.data
    
    def _staff(self, endpoint: str, params: dict, data: dict):
        result: Result = self.method(
            endpoint=endpoint,
            params=params,
            data=data,
        )
        return result.data
    
    def _labor_codes(self, endpoint: str, params: dict, data: dict):
        result: Result = self.method(
            endpoint=endpoint,
            params=params,
            data=data,
        )
        return result.data
    
    def _expense_codes(self, endpoint: str, params: dict, data: dict):
        result: Result = self.method(
            endpoint=endpoint,
            params=params,
            data=data,
        )
        return result.data
    
    def _expense_code(self, endpoint: str, params: dict, data: dict):
        result: Result = self.method(
            endpoint=endpoint,
            params=params,
            data=data,
        )
        return result.data
    
    def _all_tasks_by_project(self, endpoint: str, params: dict, data: dict):
        result: Result = self.method(
            endpoint=endpoint,
            params=params,
            data=data,
        )
        return result.data
    
    def _estimates_by_projects(self, endpoint: str, params: dict, data: dict):
        result: Result = self.method(
            endpoint=endpoint,
            params=params,
            data=data,
        )
        return result.data
    
    def _tasks_by_project(self, endpoint: str, params: dict, data: dict):
        result: Result = self.method(
            endpoint=endpoint,
            params=params,
            data=data,
        )
        return result.data
    
    def _qb_classes(self, endpoint: str, params: dict, data: dict):
        result: Result = self.method(
            endpoint=endpoint,
            params=params,
            data=data,
        )
        return result.data
    
    def _payroll_items(self, endpoint: str, params: dict, data: dict):
        result: Result = self.method(
            endpoint=endpoint,
            params=params,
            data=data,
        )
        return result.data
    
    def _field_values(self, endpoint: str, params: dict, data: dict):
        result: Result = self.method(
            endpoint=endpoint,
            params=params,
            data=data,
        )
        return result.data
    
    def _qb_account_list(self, endpoint: str, params: dict, data: dict):
        result: Result = self.method(
            endpoint=endpoint,
            params=params,
            data=data,
        )
        return result.data
    
    def _qb_list(self, endpoint: str, params: dict, data: dict):
        result: Result = self.method(
            endpoint=endpoint,
            params=params,
            data=data,
        )
        return result.data
    
    def _ia_list(self, endpoint: str, params: dict, data: dict):
        result: Result = self.method(
            endpoint=endpoint,
            params=params,
            data=data,
        )
        return result.data
    
    def _task_status(self, endpoint: str, params: dict, data: dict):
        result: Result = self.method(
            endpoint=endpoint,
            params=params,
            data=data,
        )
        return result.data
    
    def _task_priority(self, endpoint: str, params: dict, data: dict):
        result: Result = self.method(
            endpoint=endpoint,
            params=params,
            data=data,
        )
        return result.data
    
    def _expense_type(self, endpoint: str, params: dict, data: dict):
        result: Result = self.method(
            endpoint=endpoint,
            params=params,
            data=data,
        )
        return result.data
    
    def _invoice_types(self, endpoint: str, params: dict, data: dict):
        result: Result = self.method(
            endpoint=endpoint,
            params=params,
            data=data,
        )
        return result.data
    
    def _credit_cards(self, endpoint: str, params: dict, data: dict):
        result: Result = self.method(
            endpoint=endpoint,
            params=params,
            data=data,
        )
        return result.data
    
    def _time_zones(self, endpoint: str, params: dict, data: dict):
        result: Result = self.method(
            endpoint=endpoint,
            params=params,
            data=data,
        )
        return result.data
    