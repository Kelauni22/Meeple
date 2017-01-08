from django.shortcuts import render
from django.http import HttpResponse

def home(request): #This is a view in Django
    return render(request, "main/home.html", {
        'message': 'This is so cool!'
    })
    #this is a dictionary where you define variable that you put in your template
