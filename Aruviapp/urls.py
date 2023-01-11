from django.contrib import admin
from django.urls import path
from .import views

urlpatterns=[
    path('home/',views.home,name='home'),
    path('course/',views.course,name='course'),
    path('gallery/',views.gallery,name='gallery'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
]