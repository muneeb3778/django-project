from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt                # decorator funciton for csrf varification
from io import BytesIO
from rest_framework.parsers import JSONParser
from .serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# Create your views here.

@csrf_exempt
def createstudentdata(request):      # creating student data in django model by json
    if request.data =='POST':
        json_data=request.body       # yaha json data ajayga ab ise stream me convert karke hi python data me convert kar sakte he
        stream=BytesIO(json_data)    # yaha json data srteam me convert ho gaya
        python_data=JSONParser().parse(stream) # stream ko python data me convert karne ke liye JSONParser() ke parse function ko call karna hoga ab python data ko complex data me convert karna hoga
        complex_data=StudentSerializer(data=python_data)  # yaha complex data me convert ho jayga
        if (complex_data.is_valid):     # agar sahi hoga to ye chal jayga
             complex_data.save()          
             response={'message':'your data have been save'} # ab ye dict he isko json me convert karke bhejenge data
             json_dataa=JSONRenderer().render(response)      # yaha json me convert ho gaya
             return HttpResponse(json_dataa,content_type='application/json')
    
    return HttpResponse("this is get request")










