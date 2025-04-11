from .models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.shortcuts import render, redirect
# Create your views here.

def user_login(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username,password=password)

        if(user):
            login(request,user)
            messages.success(request,"login successfull !")
            return redirect('dashboard')
        else:
            messages.error(request,"no user")
            
    return render(request,'login.html',{})

def user_logout(request):
    logout(request)
    return redirect('userlogin')