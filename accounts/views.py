from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages,auth
# Create your views here.

def login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,"you are logged in")
            return redirect('home')
        else:
            messages.error(request,"invalid credentials")
            return redirect('login')
    
    return render(request, 'accounts/login.html')

def register(request):
    if request.method=="POST":
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
                
        if(password==confirm_password):
            if User.objects.filter(username=username).exists():
                messages.error(request,"Username exists")
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,"email already exists")
                else:
                    user=User(first_name=firstname,last_name=lastname,username=username,email=email,password=password)
                    user.save()
                    messages.success(request,"Account Created Successfully")
                    return redirect('login')
        else:
            messages.success(request,"Password do not match")
    return render(request, 'accounts/register.html')

def logout_user(request):
    logout(request)
    return redirect('home')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')