from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('createstudent/', views.createstudentdata),
    path('studentapi/', views.stundent_api),
    
]

















