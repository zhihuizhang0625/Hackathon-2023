import requests

AIRTABLE_BASE_ID = ''
AIRTABLE_API_KEY= 
AIRTABLE_TABLE_NAME =

endpoint = f''

#python requests headers
def add_to_airtable(email = None, name = ""):
    if email is None:
        return 
        headers = {"Authorization": f"Bearer {AIRTABLE_API_KEY}",
        "Content-Type": "application/json"
        }

        data = {

        }

        r= requests.post(endpoint, json = data, headers = headers)
        print(r.status_code)