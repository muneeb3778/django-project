from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt                # decorator funciton for csrf varification
from io import BytesIO
from rest_framework.parsers import JSONParser
from .serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse , JsonResponse
from .models import Student
# muneeb abdullah hamza saad 
# Create your views here.
# ye function base view he

@csrf_exempt                         # ye expect kar raha he crft token jese django form me expect karta he csrf token
def createstudentdata(request):      # creating student data in django model by json
    if request.method =='POST':
        json_data=request.body       # yaha json data ajayga ab ise stream me convert karke hi python data me convert kar sakte he
        stream=BytesIO(json_data)    # yaha json data srteam me convert ho gaya
        python_data=JSONParser().parse(stream) # stream ko python data me convert karne ke liye JSONParser() ke parse function ko call karna hoga ab python data ko complex data me convert karna hoga
        complex_data=StudentSerializer(data=python_data)  # yaha complex data me convert ho jayga
        if (complex_data.is_valid()):     # agar sahi hoga to ye chal jayga matlab ke data base me save karne ke layak he nahi he
             complex_data.save()          
             response={'message':'your data have been save'} # ab ye dict he isko json me convert karke bhejenge data
             json_dataa=JSONRenderer().render(response)      # yaha json me convert ho gaya
             return HttpResponse(json_dataa,content_type='application/json')     # jab bhi HttpResponse me json likhte he to usme content_type='application/json' ye likhna zaruri hota he
        json_dataa = JSONRenderer().render(complex_data.errors)
        return HttpResponse(json_dataa,content_type='application/json')  
    return HttpResponse("this is get request")

# aur ye tab chalega jab bhi frontend se post request aaygi aur frontent kuch bhi ho sakta he python react javascript etc
# aur ye iska jo frontend is myproject me kaam nahi kar rahi ti to alag se python folder me myapp.py file banai aur waha se post request bheji he



@csrf_exempt
def stundent_api(request):
    if request.method == 'GET':
        json_data =request.body                                # waha jo bhi data likha he vo isme ajayga
        stream=BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id = python_data.get('id',None)                        # iska matlab agar id di he to uski value id me daldo nahi to none daldo
        if id is not None:
            stu = Student.objects.get(id=id)
            complex_data=StudentSerializer(stu)
            json_dataa=JSONRenderer().render(complex_data.data)
            return HttpResponse(json_dataa,content_type='application/json')
        else:
          stu=Student.objects.all()
          complex_data= StudentSerializer(stu,many=True)
          print(complex_data.data,'rehamnnnnnnnnnnnnnnnnnnnnnnnnnnnnnssssssssssssssss')
          json_dataa=JSONRenderer().render(complex_data.data)
          return HttpResponse(json_dataa,content_type='application/json')
        
    if request.method =='PUT':
        json_data=request.body
        stream=BytesIO(json_data) 
        python_data=JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id=id)
        complex_data = StudentSerializer(stu,data=python_data,partial=True)         # partial=True ye isliye likha he taki partially bhi update kar sake
        if (complex_data.is_valid()):
            complex_data.save()
            res={'msg','data updated'}
            json_dataa=JSONRenderer().render(res)
            return HttpResponse(json_dataa,content_type='application/json')   
        json_dataa = JSONRenderer().render(complex_data.errors)
        return HttpResponse(json_dataa,content_type='application/json')  


    if request.method =='DELETE': 
        json_data=request.body
        stream=BytesIO(json_data) 
        python_data=JSONParser().parse(stream)
        rollno = python_data.get('rollno')
        stu = Student.objects.get(rollno=rollno)
        stu.delete()
        res={'msg','data delete'}
        # json_dataa=JSONRenderer().render(res)
        # return HttpResponse(json_dataa,content_type='application/json')   
        return JsonResponse(res,safe=False)                                         # agar upar ki 2 line nahi likhna chate to ye likhenge



