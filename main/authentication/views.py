from .models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect


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


from .forms import SignUPForm


def signup(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = SignUPForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
           username = form.cleaned_data["your_name"]
           try:
               user= User.objects.get(username=username)
               if(user):
                   print("user already exits!")
               user = User.objects.create(username=username)
               return HttpResponseRedirect("/login")
           except User.DoesNotExist:
               print("user does not exists")
               user=None
           # redirect to a new URL:  
        return HttpResponseRedirect("signup/") 

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SignUPForm()

    return render(request, "signup.html", {"form": form})