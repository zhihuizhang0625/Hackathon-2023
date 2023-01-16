import requests

AIRTABLE_BASE_ID = 'appJQ2e3Bms1nlD3B'
AIRTABLE_API_KEY= 'keyQ0V1l9vBkHkLev'
AIRTABLE_TABLE_NAME ='leetcode_analysis'
AIRTABLE_OAUTH = 'patCSzdYGtv19W5R4.0958fccfc23a810a713ba93534c6c45f4dfe9f4cbeadd45dfbb65b290a73652f'

# create table
def create_table():
    endpoint = f'https://api.airtable.com/v0/meta/bases/{AIRTABLE_BASE_ID}/tables'
    headers = {
        "Authorization": "Bearer " + str(AIRTABLE_OAUTH),
        "Content-Type": "application/json"
        }

    data =  {
    "description": "Testing create_table2",
    "fields": [
      {
        "description": "Problem name",
        "name": "title",
        "type": "singleLineText"
      },
      {
        "name": "link",
        "type": "singleLineText"
      },
      {
        "name": "difficulty",
        "type": "singleLineText"
      },
      {
        "name": "status",
        "type": "singleLineText"
      }
    ],
    "name": "Test3"
  }       

    r= requests.post(endpoint, json = data, headers = headers)
    print(r)
    
# import records
def add_to_airtable(name = "", email = None):
    endpoint = f'https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}'
    if email is None:
        return 
    headers = {
        "Authorization": "Bearer " + str(AIRTABLE_API_KEY),
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
    print(r)

#  update records
def update_records():
    endpoint = f'https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}'
    headers = {
        "Authorization": "Bearer " + str(AIRTABLE_API_KEY),
        "Content-Type": "application/json"
        }

    data = {
    "records": [
      {
        "fields": {
          "Name": "def",
          "Email": "abc@gmail.com"
        },
        "id": "recqhmz9ZSZFSh8WP"
      },
      {
        "fields": {
          "Name": "clara",
          "Email": "wefsv@gmail.com"
        },
        "id": "recd0xzqL0uI098WH"
      }
    ]
  } 

    r= requests.patch(endpoint, json = data, headers = headers)
    print(endpoint)
    
    print(r)
    

create_table()
add_to_airtable("abc", "abc@gmail.com")
update_records()

