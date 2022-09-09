import requests
import json

URL='http://127.0.0.1:8000/student_api/'

#to retrieve data
def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
    json_data=json.dumps(data)
    r=requests.get(url=URL,data=json_data)
    data=r.json()
    print(data)
#for all data
#get_data()
#for specific id
#get_data(1)


#To POST data
def post_data():
    data={
        'name':'Ravi',
        'roll':205,
        'city':'Banglore'
    }
    json_data=json.dumps(data)
    r=requests.post(url=URL,data=json_data)
    data=r.json()
    print(data)
#post_data()

#Update Request
def Update_data():
    data={
        'id':6,
        'name':'Ravishankar',
        'roll':306,
        'city':'Hyderabad'
    }
    json_data=json.dumps(data)
    r=requests.put(url=URL,data=json_data)
    data=r.json()
    print(data)
    
Update_data()

#Delete Data
def Delete_data():
    data={'id':8}
    json_data=json.dumps(data)
    r=requests.delete(url=URL,data = json_data)
    data=r.json()
    print(data)

#Delete_data()