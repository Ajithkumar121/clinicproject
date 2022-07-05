from django.shortcuts import render,redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request,"index.html")


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['pass']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "invalid username")
            return redirect('login')
    return render(request, "login.html")

def registration(request):
    if request.method=='POST':
        username=request.POST['username']
        # first_name= request.POST['firstname']
        # last_name = request.POST['lastname']
        email = request.POST['email']
        password1 = request.POST['pass']
        password2= request.POST['confirm-pass']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username Taken")
                return redirect("/login")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email Taken")
                return redirect("registration")
            else:
                user=User.objects.create_user(username=username,email=email,password=password1)
                user.save()
                # return redirect('/login')
        else:
            messages.info(request,"password not matched")
            return redirect('registration')

    return render(request,"registration.html")

def details(request):
    return render(request,"details.html")


def logout(request):
    auth.logout(request)
    return redirect('/')

def book(request):
    return render(request,"book.html")
