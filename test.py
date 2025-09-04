from dotenv import load_dotenv
from os import environ

from api_wrapper.bigtime_api import BigTimeAPI

load_dotenv()

firm_id = environ["FIRM"]
api_key = environ["API"]
staff_id = environ["TEST_STAFF_ID"]
print(staff_id)

api = BigTimeAPI(api_key=api_key, firm=firm_id)

staff_list = api.get_picklist_staff()
print(staff_list)

project_list = api.get.picklist.projects(staff_sid=staff_id)

print(project_list)