from django.shortcuts import render,redirect
from .models import*
from django.contrib  import messages
from.forms import RegisterStudent
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request,'index.html')

def course(request):
    return render(request,'Course.html')

def gallery(request):
    return render(request,'Gallery.html')

def about(request):
    return render(request,'About.html')

def contact(request):
    return render(request,'Contact.html')

# def register(request):
#     if request.method=="POST":
#         name=request.POST['name']
#         mobile=request.POST['mobile']
#         email=request.POST['email']
#         date_of_birth=request.POST['date_of_birth']
#         gender=request.POST['gender']
#         age=request.POST['age']
#         passed_year=request.POST['passed_year']
#         degree=request.POST['degree']
#         course=request.POST['course']
        

#         myuser=User.objects.create_user(name,email,mobile)
#         myuser.save()
#         return redirect('register')
#     return render(request,"Register.html")

def register(request):
    myuser=RegisterStudent(request.POST or None)
    if myuser.is_valid():
        myuser.save()
        messages.success(request,"Welcome To Our AruviFamily")
        return redirect('register')
    return render(request,"Register.html",{"form": myuser})

