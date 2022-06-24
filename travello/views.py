from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.

from .models import Destination

def index(request):

    # dest1 = Destination()
    # dest1.name = 'Mumbai'
    # dest1.desc = 'The City That Never Sleep'
    # dest1.price = 7000
    # dest1.img = 'destination_1.jpg'
    # dest1.offer = True
    #
    # dest2 = Destination()
    # dest2.name = 'America'
    # dest2.desc = 'The USA Powerful Country'
    # dest2.price = 12000
    # dest2.img = 'destination_2.jpg'
    # dest2.offer = False
    #
    # dest3 = Destination()
    # dest3.name = 'Canada'
    # dest3.desc = 'The Country Of Panjabi'
    # dest3.price = 9000
    # dest3.img = 'destination_3.jpg'
    # dest3.offer = True

    # dests= [dest1,dest2,dest3]
    dests= Destination.objects.all()




    return render(request,'index.html',{'dests': dests })



def about(request):
    return render(request,'about2.html')















# def index(request):
#     # dect = {'name':'Ankit','addr':'Mars'}
#     return render(request,'index.html',{'price':700})
    # return HttpResponse("Hellow world")


# def add(request):
#     val1 = int(request.POST['num1'])
#     val2 = int(request.POST['num2'])
#     res = val1+val2
#
#     return render(request,'result.html',{'result':res})
