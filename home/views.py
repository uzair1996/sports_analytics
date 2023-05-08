from django.shortcuts import render, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
#def home(request):
    #return HttpResponse("This is my homepage (/)")
 #   context = {'name':'harry','course':'Django'}
  #  return render(request,"home.html",context)

def about(request):
    #return HttpResponse("This is my about page (/)")
    return render(request,"about.html")

def project(request):
    #return HttpResponse("This is my project page (/)")
    return render(request,"project.html")
def contact(request):
    #return HttpResponse("This is my contact page (/)")
    return render(request,"contact.html")

def movies(request):
    #moviesstr = Movies.objects.all() #queryset containing all movies we just created
    #return render(request=request, template_name="main/movies.html", context={'movies':movies})
    return HttpResponse("<h1> hsjbcsxcsccs </h1>")

@login_required(login_url='login')
def home(request):
    return render(request,"home.html")

@login_required(login_url='login')
def series(request):
    return render(request,"series.html") 

@login_required(login_url='login')
def player(request):
    return render(request,"player.html")     

@login_required(login_url='login')
def matches(request):
    return render(request,"matches.html")

@login_required(login_url='login')
def tableau(request):
    return render(request,"tableau.html")    

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1!=pass2:
            return HttpResponse("Password and confirm Password does not match please try again!!")

        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    return render(request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Wrong username or password")

    return render(request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login') 

 