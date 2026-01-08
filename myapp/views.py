from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login,logout
from django.contrib.auth.decorators import login_required,user_passes_test
from myapp.models import Lugat
from django.contrib.auth.models import User

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")  
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})

def user_login(request):
    if request.user.is_authenticated:
        return redirect("home")  

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()        
            auth_login(request, user)     
            return redirect("home")
        else:
            form.add_error(None, "Invalid username or password")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

@login_required
def log_out(request):
    logout(request)
    return redirect("login")


@login_required
def add_word(request):
    if request.method == "POST":
        Lugat.objects.create(
            user=request.user, 
            word=request.POST.get("word"),
            definition=request.POST.get("definition"),
            meaning=request.POST.get("meaning"),
        )
    return redirect("home")



@login_required
def input(request):
    words = Lugat.objects.filter(user=request.user)  
    return render(request, "input.html", {"words": words})
@login_required
@user_passes_test(lambda u: u.is_superuser)
def get_users(request):
    users= User.objects.all()
    return render(request,'users.html',{"users": users})

