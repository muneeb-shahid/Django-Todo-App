from django.shortcuts import render
from django.http import HttpResponse

def members(request):
    return HttpResponse("Hello world!")

def addToDo(request):
    return HttpResponse("Hello addToDo!")

def calculation(request):
    # a= 12
    # b=8
    # calculation = a+b
    print("Calculator") 


    math = int(input("Enter marks of the math subject: "))
    Urdu = int(input("Enter marks of the Urdu subject: "))
    isl = int(input("Enter marks of the isl subject: "))
    eng = int(input("Enter marks of the eng subject: "))
    chem = int(input("Enter marks of the chem subject: "))

    obtainedMark = math+ Urdu+ isl+eng+chem
    totalMark = 500

    percentage = (obtainedMark/totalMark)* 100
    print("The percentage is: ",percentage)

    if(percentage > 90):
        print("A+ Grade")
    elif(percentage > 80 and percentage <90  ):
        print("A Grade")
    # return HttpResponse("calculation: " + str(a) +"+"+ str(b) + '=' + str(calculation))
    return HttpResponse("The percentage is: " + str(percentage))
