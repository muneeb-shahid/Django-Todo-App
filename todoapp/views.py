from django.shortcuts import render
from django.http import HttpResponse

def members(request):
    return HttpResponse("Hello world!")

def addToDo(request):
    return HttpResponse("Hello addToDo!")

def calculation(request):
    a= 12
    b=8
    calculation = a+b
    return HttpResponse("calculation: " + str(a) +"+"+ str(b) + '=' + str(calculation))