from django.shortcuts import render
from .models import Destination




def index(request):

    dest1 = Destination()
    dest1.name = 'Karachi'
    dest1.desc = 'City of Lights'
    dest1.img = 'destination_1.jpg'
    #dest1.info = 'Axiom Education'
    dest1.price = 900
    dest1.offer = False

    dest2 = Destination()
    dest2.name = 'Lahore'
    dest2.desc = 'Eat Nehari'
    dest2.img = 'destination_2.jpg'
    #dest2.info = 'Axiom Education'
    dest2.price = 700
    dest2.offer = False

    dest3 = Destination()
    dest3.name = 'Islamabad'
    dest3.desc = 'Clean City , Captial'
    dest3.img = 'destination_3.jpg'
    #dest3.info = 'Axiom Education'
    dest3.price = 1000
    dest3.offer = True

    dest4 = Destination()
    dest4.name = 'Peshware'
    dest4.desc = 'Pista , Badaam'
    dest4.img = 'destination_4.jpg'
    #dest4.info = 'Axiom Education'
    dest4.price = 150
    dest4.offer = True

    dest5 = Destination()
    dest5.name = 'Quetta'
    dest5.desc = 'Damphook'
    dest5.img = 'destination_5.jpg'
    #dest5.info = 'Axiom Education'
    dest5.price = 290
    dest5.offer = False
    
    dest6 = Destination()
    dest6.name = 'Hyderabad'
    dest6.desc = 'Eat Karahi'
    dest6.img = 'destination_6.jpg'
    #dest6.info = 'Axiom Education'
    dest6.price = 250
    dest6.offer = False


    dests = [dest1 , dest2 , dest3 , dest4 , dest5 , dest6]


    return render(request , 'index.html' , {'FinDest':dests})

# Create your views here.
