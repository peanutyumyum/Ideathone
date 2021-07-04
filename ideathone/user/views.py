from django import forms
from django.shortcuts import redirect, render

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

from django.utils import timezone

from .models import Blog, CustomUser
from .forms import BlogForm, RegistorForm

def main(request):
    return render(request, "main.html")

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data = request.POST)
        if form.is_valid(): #유효성 검사
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request=request, username = username, password=password)
            if user is not None :
                login(request, user)
            return redirect("main:main")
    else :
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form}) #Get방식

def logout_view(requset):
    logout(requset)
    return redirect("main:main")

def signup_view(request):
    if request.method == "POST": #요청방식이 POST
        form = RegistorForm(request.POST)
        if form.is_valid(): #form 유효성 검사
            user = form.save()
            login(request, user)
            return redirect("main:main")
        else:
            print("vaild하지 않")
            return redirect("main:main")
    else: #요청방식이 GET
        form = RegistorForm()
    return render(request, 'signup.html', {'form':form})


def create_page(request):
    forms = BlogForm()
    context = {
        'forms' : forms,
    }
    return render(request, 'create.html',context)

def create(request):
    form = BlogForm(request.POST,request.FILES)
    if form.is_valid():
        new_blog = form.save(commit=False)
        new_blog.pub_date = timezone.now()
        new_blog.save()
    return redirect('main.html')