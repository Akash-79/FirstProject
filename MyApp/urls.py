
from django.contrib import admin
from django.urls import path
from MyApp import views as v
urlpatterns = [
    path('hello',v.home),
    path('',v.index),
    path('register',v.register),
    path('empList',v.empList),
    path('third',v.third),
    path('addUser',v.addUser),
    path('deleteEmp',v.deleteEmp),
    path('editEmp',v.editEmp),
    path('updateEmp',v.updateEmp),

]
