from django.shortcuts import render,HttpResponse
from webpages.models import Contact,Slider,Car
from rest_framework.decorators import api_view
import json
from django.http import JsonResponse
# Create your views here.
def index(request):
    slider=Slider.objects.all()
    data={
        'slider':slider,
    }
    return render(request, 'webpages/home.html',data)

def contact(request):
    if request.method == "POST":
        first_name=request.POST.get('firstname')
        last_name=request.POST.get('lastname')
        email=request.POST.get('email')
        number=request.POST.get('number')
        obj=Contact(first_name=first_name,last_name=last_name,email=email,number=number)
        obj.save()
        print("this is data")
        print(first_name,last_name,email,number)
       
    return render(request, 'webpages/contact.html')

def about(request):
    return render(request, 'index.html')
def services(request):
    return render(request, 'index.html')
def features(request):
    return render(request, 'index.html')


@api_view(["POST"])
def calculater(h):
    data=json.loads(h.body)
    num={}
    if(data['w']=='+'):
        num['add']=data["a"]+data["b"]
    return JsonResponse(num,safe=False)

@api_view(["GET"])
def car(request):
    car=Car.objects.get()
    # d=json.load(car)
    print(car.name)
    return JsonResponse("car name:"+str(car.name)+" AND "+"car max_speed:"+str(car.max_speed),safe=False)


