import requests

AIRTABLE_BASE_ID = 'appJQ2e3Bms1nlD3B'
AIRTABLE_API_KEY= 'YOUR_API_KEY'
AIRTABLE_TABLE_NAME ='leetcode_analysis'

endpoint = f'https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}'

#python requests headers
def add_to_airtable(email = None, name = ""):
    if email is None:
        return 
        headers = {"Authorization": "Bearer {AIRTABLE_API_KEY}",
        "Content-Type": "application/json"
        }

        data =  {
          "records": [
            {
              "fields": {
                "Name": name,
                "Email": email
              }
            }
     
          ]
        }       

        r= requests.post(endpoint, json = data, headers = headers)
        print(r.status_code)


add_to_airtable("abc", "abc@gmail.com")
