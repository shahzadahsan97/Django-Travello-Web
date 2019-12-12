from django.shortcuts import render
from .models import Destination




def index(request):

    dest1 = Destination()
    dest1.name = 'Karachi'
    dest1.desc = 'City of Lights'
    dest1.price = 100

    return render(request , 'index.html' , {'Dest1':dest1})

# Create your views here.
