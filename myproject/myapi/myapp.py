import requests
from json import dumps            # ye json format me convert kar deta he

URL ='http://127.0.0.1:8000/createstudent/'
dataa={
'name':'muneeb ur rehman',
'rollno':50,
'city':'bhopal'
}




json_data=dumps(dataa)
response=requests.post(url=URL, data=json_data)
print(response.json())




