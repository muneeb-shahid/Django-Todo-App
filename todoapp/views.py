from django.shortcuts import render
from django.http import HttpResponse

def members(request):
    return HttpResponse("Hello world!")

def addToDo(request):
    return HttpResponse("Hello addToDo!")

def calculation(request):
    calculation = 12+8
    return HttpResponse("calculation : " + str(calculation))