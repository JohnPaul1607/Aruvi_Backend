from django.shortcuts import render

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