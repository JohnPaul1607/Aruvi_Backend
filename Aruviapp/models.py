from django.db import models
from django.conf import settings

# Create your models here.

class student(models.Model):
    name=models.CharField(max_length=100)
    mobile=models.CharField(max_length=12)
    email=models.EmailField(max_length=100)
    date_of_birth=models.DateField(null=True)
    Gender_choise=(
        ("Male","Male"),
        ("Female","Female"),
    )
    age=models.IntegerField()
    gender=models.CharField(choices=Gender_choise,max_length=10)
    academic_year=models.CharField(max_length=10)
    degree=models.CharField(max_length=100)
    Course_choise=(
        ("Python","Python"),
        ("Java","Java"),
        ("Django","Django"),
        ("Web Development","Web Development"),
        ("Data Science","Data Science in Python"),
        ("Machine Learning","Machine Learning"),
        ("Full Stack Web Development","Full Stack Web Development"),
        ("C Programming","C Programming"),
        ("DataBase","DataBase"),
    )
    course=models.CharField(choices=Course_choise,max_length=100)
