from django.shortcuts import render,redirect
from .models import student
from django.contrib  import messages
from.forms import RegisterStudent
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import get_list_or_404
from rest_framework.response import Response
from rest_framework import status
from.serializers import studentSerializer
from rest_framework.decorators import api_view
from django.core.mail import send_mail
from django.conf import settings

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

def register(request):
    myuser=RegisterStudent(request.POST)
    if myuser.is_valid():
        myuser.save()
        username=myuser.cleaned_data.get('name')
        messages.success(request,f' Hi {username} , thank you for register in Aruvi Institute of Learning.  Welcome to Aruvi')

        return redirect('register')
    return render(request,"Register.html",{"form": myuser})


# class studentlist(APIView):
@api_view(['GET','POST'])
def studentlist(request,format=None):
    if request.method=='GET':
        stu=student.objects.all()
        serializer=studentSerializer(stu,many=True)
        return Response(serializer.data)
    if request.method=='POST':
        serializer=studentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def studentdetails(request,pk,format=None):
    try:
        stud=student.objects.get(pk=pk)
    except stud.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializer=studentSerializer(stud)
        return Response(serializer.data)

    elif request.method=='PUT':
        serializer=studentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
        
    elif request.method=='DELETE':
        student.delete(stud)
        return Response(status=status.HTTP_404_NOT_FOUND)




