import requests
import json
  


AIRTABLE_BASE_ID = 'appJQ2e3Bms1nlD3B'
AIRTABLE_API_KEY= 'keyQ0V1l9vBkHkLev'
#AIRTABLE_TABLE_NAME =''
AIRTABLE_OAUTH = 'patCSzdYGtv19W5R4.0958fccfc23a810a713ba93534c6c45f4dfe9f4cbeadd45dfbb65b290a73652f'

# table1 -create add update
# create table
def create_table1(AIRTABLE_TABLE_NAME = ''):
    endpoint = f'https://api.airtable.com/v0/meta/bases/{AIRTABLE_BASE_ID}/tables'
    headers = {
        "Authorization": "Bearer " + str(AIRTABLE_OAUTH),
        "Content-Type": "application/json"
        }

    data =  {
    "description": "create_table1",
    "fields": [
      {
        "description": "Problem name",
        "name": "title",
        "type": "singleLineText",
      },
      {
        "name": "link",
        "type": "singleLineText",
      },
      {
        "name": "difficulty",
        "type": "singleLineText",
      },
      {
        "name": "status",
        "type": "singleLineText",
      },
      {
        "name": "submission",
        "type": "singleLineText",
      },
      {
        "name": "submission_times",
        "type": "singleLineText",
      }
   
    
    ],
    "name": AIRTABLE_TABLE_NAME
  }       

    r= requests.post(endpoint, json = data, headers = headers)
    print(r)
    
# import records
def add_to_airtable1(title = "", link = None, difficulty = None, status = None, submission_history = None, submission_times = None, AIRTABLE_TABLE_NAME = ''):
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
                "submission": submission_history,
                "submission_times": submission_times,
              }
            }
     
          ]
        }       

    r= requests.post(endpoint, json = data, headers = headers)
    print(r)

#  update records
def update_records1(AIRTABLE_TABLE_NAME = ''):
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
    


#table 2
# table1 -create add update
# create table
def create_table2(AIRTABLE_TABLE_NAME = ''):
    endpoint = f'https://api.airtable.com/v0/meta/bases/{AIRTABLE_BASE_ID}/tables'
    headers = {
        "Authorization": "Bearer " + str(AIRTABLE_OAUTH),
        "Content-Type": "application/json"
        }

    data =  {
    "description": "create_table2",
    "fields": [
      {
        "description": "Submission history",
        "name": "last_submission_status",
        "type": "singleLineText",
      },
      {
        "name": "last_submission_time",
        "type": "singleLineText",
      },
      {
        "name": "last_2th_submission_status",
        "type": "singleLineText",
      },
      {
        "name": "last_2th_submission_time",
        "type": "singleLineText",
      },
      {
        "name": "last_3th_submission_status",
        "type": "singleLineText",
      },
      {
        "name": "last_3th_submission_time",
        "type": "singleLineText",
      },
      {
        "name": "last_4th_submission_status",
        "type": "singleLineText",
      },{
        "name": "last_4th_submission_time",
        "type": "singleLineText",
      },{
        "name": "last_5th_submission_status",
        "type": "singleLineText",
      },{
        "name": "last_5th_submission_time",
        "type": "singleLineText",
      },
   
    
    ],
    "name": AIRTABLE_TABLE_NAME
  }       

    r= requests.post(endpoint, json = data, headers = headers)
    print(r)
    
# import records
def add_to_airtable2(sub1_status = None, sub1_time = None, sub2_status = None, sub2_time = None,sub3_status = None, sub3_time = None,sub4_status = None, sub4_time = None,sub5_status = None, sub5_time = None, AIRTABLE_TABLE_NAME = ''):
    endpoint = f'https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}'
    headers = {
        "Authorization": "Bearer " + str(AIRTABLE_API_KEY),
        "Content-Type": "application/json"
        }

    data =  {
          "records": [
            {
              "fields": {
                "last_submission_status": sub1_status,
                "last_submission_time": sub1_time,
                "last_2th_submission_status": sub2_status,
                "last_2th_submission_time": sub2_time,
                "last_3th_submission_status": sub3_status,
                "last_3th_submission_time": sub3_time,
                "last_4th_submission_status": sub4_status,
                "last_4th_submission_time": sub4_time,
                "last_5th_submission_status": sub5_status,
                "last_5th_submission_time": sub5_time,
                
                
                
                
              }
            }
     
          ]
        }       

    r= requests.post(endpoint, json = data, headers = headers)
    print(r)

#  update records
def update_records2(sub1_status = None, sub1_time = None, sub2_status = None, sub2_time = None,sub3_status = None, sub3_time = None,sub4_status = None, sub4_time = None,sub5_status = None, sub5_time = None,AIRTABLE_TABLE_NAME = ''):
    endpoint = f'https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}'
    headers = {
        "Authorization": "Bearer " + str(AIRTABLE_API_KEY),
        "Content-Type": "application/json"
        }

    data = {
    "records": [
      {
         "fields": {
                "last_submission_status": sub1_status,
                "last_submission_time": sub1_time,
                "last_2th_submission_status": sub2_status,
                "last_2th_submission_time": sub2_time,
                "last_3th_submission_status": sub3_status,
                "last_3th_submission_time": sub3_time,
                "last_4th_submission_status": sub4_status,
                "last_4th_submission_time": sub4_time,
                "last_5th_submission_status": sub5_status,
                "last_5th_submission_time": sub5_time,
                
        },
        "id": "recqhmz9ZSZFSh8WP"
      }
    ]
  } 

    r= requests.patch(endpoint, json = data, headers = headers)
    print(endpoint)
    
    print(r)
    


    r= requests.post(endpoint, json = data, headers = headers)
    print(r)


def load_sample():
    create_table1('summary')
    create_table2('submission_history')
    create_table1('failed_problems')

    # Opening JSON file
    f = open('sample.json')
    f2 = open('failed.json')
    
    # returns JSON object as 
    # a dictionary
    data = json.load(f)
    failed_data = json.load(f2)
      
    #print(data)
    # Iterating through the json
    # list
    for i in data:
      add_to_airtable1(i['title'], i['link'],i['difficulty'],i['status'],str(i['submission_history']),i['submission_times'], 'summary')
      
      if(len(i['submission_history']) < 5):

        sub_status = []
        sub_time = []
        num = len(i['submission_history'])

        for j in range(num):
          #print(j)
          sub_status.append(i['submission_history'][-(j+1)]['submission_status'])
          print(sub_status[j])
          sub_time.append(i['submission_history'][-(j+1)]['submission_time'])
        
        for k in range(num , 5) :
          sub_status.append(None)
          sub_time.append(None)

        add_to_airtable2(sub_status[0], sub_time[0], sub_status[1], sub_time[1], sub_status[2], sub_time[2], sub_status[3], sub_time[3], sub_status[4], sub_time[4], 'submission_history')

      else: add_to_airtable2(i['submission_history'][-1]['submission_status'],\
                          i['submission_history'][-1]['submission_time'],\
                          i['submission_history'][-2]['submission_status'],\
                          i['submission_history'][-2]['submission_time'],\
                          i['submission_history'][-3]['submission_status'],\
                          i['submission_history'][-3]['submission_time'],\
                          i['submission_history'][-4]['submission_status'],\
                          i['submission_history'][-4]['submission_time'],\
                          i['submission_history'][-5]['submission_status'],\
                          i['submission_history'][-5]['submission_time'],\
                          'submission_history')


    # Closing file
    f.close()
    
    for i in data:
      add_to_airtable1(i['title'], i['link'],i['difficulty'],i['status'],str(i['submission_history']),i['submission_times'], 'failed_problems')
      
                 


    # Closing file
    f2.close()

#load sample
load_sample()