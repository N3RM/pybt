from api_wrapper.models import Result

class AsyncEndPoint:
    def __init__(self, method: callable, params: list, data: dict) -> None:
        self.method = method
        self.endpoint = "/Async"
        self.params = params
        self.data = data

    def _ticket(self) -> dict: # Update to "Ticket" once the model is implemented
        """
        Retrieves the status of an async job
        """
        self.endpoint += "/Ticket"
        response: Result = self.method(endpoint=self.endpoint, params=self.params, data=self.data)
        result = response.data # Ticket(**response.data)
        return result
    
    def _submit_timesheet(self) -> dict: # Update once the model is implemented
        self.endpoint += "/SubmitTimesheet"
        response: Result = self.method(endpoint=self.endpoint, params=self.params, data=self.data)
        result = response.data 
        return result
    
    def _submit_timesheet_signed(self) -> dict: # Update once the model is implemented
        self.endpoint += "/SubmitTimesheetSigned"
        response: Result = self.method(endpoint=self.endpoint, params=self.params, data=self.data)
        result = response.data 
        return result
    
    def _resubmit_expense_report(self) -> dict: # Update once the model is implemented
        self.endpoint += "/ResubmitExpenseReport"
        response: Result = self.method(endpoint=self.endpoint, params=self.params, data=self.data)
        result = response.data 
        return result
    
    def _resubmit_time(self) -> dict: # Update once the model is implemented
        self.endpoint += "/ResubmitTime"
        response: Result = self.method(endpoint=self.endpoint, params=self.params, data=self.data)
        result = response.data 
        return result
    
    def _resubmit_all_time_by_staffer(self) -> dict: # Update once the model is implemented
        self.endpoint += "/ResubmitAllTimeByStaffer"
        response: Result = self.method(endpoint=self.endpoint, params=self.params, data=self.data)
        result = response.data 
        return result
    
    def _submit_expenses(self) -> dict: # Update once the model is implemented
        self.endpoint += "/SubmitExpenses"
        response: Result = self.method(endpoint=self.endpoint, params=self.params, data=self.data)
        result = response.data 
        return result
    
    def _post_timesheet(self) -> dict: # Update once the model is implemented
        self.endpoint += "/PostTimesheet"
        response: Result = self.method(endpoint=self.endpoint, params=self.params, data=self.data)
        result = response.data 
        return result
    
    def _post_expense_report(self) -> dict: # Update once the model is implemented
        self.endpoint += "/PostExpenseReport"
        response: Result = self.method(endpoint=self.endpoint, params=self.params, data=self.data)
        result = response.data 
        return result
    
    def _post_invoice(self) -> dict: # Update once the model is implemented
        self.endpoint += "/PostInvoice"
        response: Result = self.method(endpoint=self.endpoint, params=self.params, data=self.data)
        result = response.data 
        return result
    
    def _import_qb_time(self) -> dict: # Update once the model is implemented
        self.endpoint += "/ImportQBTime"
        response: Result = self.method(endpoint=self.endpoint, params=self.params, data=self.data)
        result = response.data 
        return result
    
    def _import_qb_invoices(self) -> dict: # Update once the model is implemented
        self.endpoint += "/ImportQBInvoices"
        response: Result = self.method(endpoint=self.endpoint, params=self.params, data=self.data)
        result = response.data 
        return result