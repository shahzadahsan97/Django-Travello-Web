from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    #return HttpResponse('Hello Django')
    return render(request , 'home.html' , {'name':'Shahzad Ahsan'}) #dlt jinga lang template 




# Create your views here.
