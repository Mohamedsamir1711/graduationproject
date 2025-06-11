
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import profil
from .models import loginpage
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import SignUpForm
from django import forms
from django.http import JsonResponse
from .serializer import LoginSerializer
from .serializer import SignupSerializer
from rest_framework.decorators import api_view
# Create your views here.

def homepage(request):
   return render(request, 'home/home.html')


def navbar(request):
    return render(request, 'home/navbar.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
           (request, user)
           messages.success(request, ("successfully Login! Welcome"))
           return redirect('home')
        else:
            messages.error(request, ("There was an error login, please try again"))
            return redirect('login')
    else:
        return render(request, 'home/login.html',{})
    

def signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
          data = form.cleaned_data
          for field_name, value in data.items():
              print(f"{field_name}: {value}")
          user = form.save()
          login(request,user)
          messages.success(request,'You have registered successfully!')
          return redirect('home')
        else:
           form.add_error(None,"Invalid username or password!")
           return redirect('signup')
    return render(request, 'home/signup.html',{'form': form})

def logout_user(request):
    logout(request)     
    messages.success(request,('You have been logged out!'))
    return redirect('home')

@api_view(['GET','POST'])
def login_user_ser(request):
        loginn = loginpage.objects.all()
        serializer = LoginSerializer(loginn, many= True)
        return JsonResponse({'Accounts' : serializer.data})

@api_view(['GET','POST'])
def signup_user_ser(request):
        signup = SignUpForm.cleaned_data
        for field_name, value in signup.items():
            print(f"{field_name}: {value}")
        serializer = SignupSerializer(signup, many= True)
        return JsonResponse({'serializer' : serializer.data})
        