from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    #return HttpResponse('Hello Django')
    return render(request , 'home.html' , {'name':'Shahzad Ahsan'})




# Create your views here.
