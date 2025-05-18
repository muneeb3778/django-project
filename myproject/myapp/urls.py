

from django.urls import path
from .views import *

urlpatterns = [
    path('',home),
    path('course/',course_view),
    path('course/<int:id>/',course_view),
    path('lesson/',lesson_view),
    path('lesson/<int:id>/',lesson_view),
    path('department/',department_view),             
    path('department/<int:id>/',department_view),    
    path('employee/',employee_view),
    path('employee/<int:id>/',employee_view),
    path('signup',register_view,),
    path('login',login_user),
    path('logout',logout_user),
    path('user/',User_database),
    path('user/<str:username>/',User_database),         # iska datatype bhi change kar sakte he int bhi rakh sakte he aur str bhi rakh sakte he aur iske argument me vohi naam aayega jo parameter me diya he
    path('jwt_login_user/',jwt_login_user),
    path('jwt_logout_user/',jwt_logout_user),

]
 

# {
#   "message": "login successfully",
#   "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ3NDA1MTMzLCJpYXQiOjE3NDc0MDQ4MzMsImp0aSI6IjRlMzllY2EzMTYwNDQ2NGJhZDAxMWFiM2FiYjZmZDk5IiwidXNlcl9pZCI6MTN9.e4qOWntgizLScpxB2XQvhm6o_5dPLGqLagZtEH47994",
#   "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc0NzQ5MTIzMywiaWF0IjoxNzQ3NDA0ODMzLCJqdGkiOiJhMTY4OTczMzk3Y2E0MDc5YWI1YTllZTJmNDg5NDY5OCIsInVzZXJfaWQiOjEzfQ.IKsegX5ATJxUj6R1_laFzbTs7dWKYKn5NSLt5ETc2ws"
# }


# superuser
# {
# "usernam":"sami12",
# "passwrd":"Samidjango@12345"
# }

# {
# "usernam":"muneeb123",
# "passwrd":"Muneebdjango@12345"
# }


# siqnup
# {
# "usernam":"rehman123",
# "passwrd":"Muneebdjango@12345"
# }

# {
# "usernam":"hamza123",
# "passwrd":"hamzadjango@12345"
# }

# {
# "usernam":"abdurrehman123",
# "passwrd":"abdurrehmandjango@12345"
# }

# superuser 
# {
# "usernam":"muneeb",
# "passwrd":"Muneebdjango@12345"
# }








