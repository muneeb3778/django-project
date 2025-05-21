import requests
from json import dumps            # ye json format me convert kar deta he

# is myapp se ye pata chal raha he jo client se data araha he ye basically frontend ke liye hota he
# aur ye python ke alava kahin aur bhi bana ho sakta he
# yaha jo ham data likhenge vo data database chale jayga
# aur browser se chalane se ye nahi jayga kyuki ye seperate application he

URL ='http://127.0.0.1:8000/createstudent/'     # ye isliye he ke kaha pe request sent karna he
dataa={
'name':'muneeb ur rehman',
'rollno':50,
'city':'bhopal'
}




json_data=dumps(dataa)   # ye python dict ko json format me convert kar deta he
requests.post(URL, data=json_data)  # ye isliye he is url pe kya send karna he
# print(response.status_code)




