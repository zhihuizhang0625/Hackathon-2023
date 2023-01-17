import requests
import json
  


AIRTABLE_BASE_ID = 'appJQ2e3Bms1nlD3B'
AIRTABLE_API_KEY= 'keyQ0V1l9vBkHkLev'
#AIRTABLE_TABLE_NAME =''
AIRTABLE_OAUTH = 'patCSzdYGtv19W5R4.0958fccfc23a810a713ba93534c6c45f4dfe9f4cbeadd45dfbb65b290a73652f'

# create table
def create_table(AIRTABLE_TABLE_NAME = ''):
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
        "type": "singleLineText",
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
    "name": AIRTABLE_TABLE_NAME
  }       

    r= requests.post(endpoint, json = data, headers = headers)
    print(r)
    
# import records
def add_to_airtable(title = "", link = None, difficulty = None, status = None, AIRTABLE_TABLE_NAME = ''):
    endpoint = f'https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}'
    headers = {
        "Authorization": "Bearer " + str(AIRTABLE_API_KEY),
        "Content-Type": "application/json"
        }

    data =  {
          "records": [
            {
              "fields": {
                "title": title,
                "link": link,
                "difficulty": difficulty,
                "status": status,
              }
            }
     
          ]
        }       

    r= requests.post(endpoint, json = data, headers = headers)
    print(r)

#  update records
def update_records(AIRTABLE_TABLE_NAME = ''):
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
    

def load_sample():
    create_table('test')

    # Opening JSON file
    f = open('sample.json')
    
    # returns JSON object as 
    # a dictionary
    data = json.load(f)
      
    #print(data)
    # Iterating through the json
    # list
    for i in data:
      add_to_airtable(i['title'], i['link'],i['difficulty'],i['status'], 'test')
      print(i)

    # Closing file
    f.close()

#load sample
load_sample()