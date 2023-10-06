from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def home(request):
    return render(request,"authentication/index.html")

def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('enrollment')
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        pass_rep = request.POST.get('pass_rep')

        if password == pass_rep:
            my_user = User.objects.create_user(uname,email,password,)
            
            name = name.split()
            my_user.first_name = name[0]
            my_user.last_name = name[1]


            my_user.save()
            messages.success(request,'Created User')

            return redirect("signin")
        else:
            messages.error(request,'Password does not match')
            return redirect('signup')

    return render(request,"authentication/signup.html")

def signin(request):
    if request.method == 'POST':
        uname = request.POST['enrollment']
        password = request.POST['password']

        user = authenticate(username=uname,password=password)

        if user is not None:
            login(request, user)
            name = user.first_name 
            return render(request,'authentication/index.html', {'name':name, })
        else:
            messages.error(request,'Bad Credentials')
            return redirect('home')

    return render(request,"authentication/signin.html")

def signout(request):
    logout(request)
    messages.success(request,'Logged Out')
    return redirect('home')