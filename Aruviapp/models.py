from django.db import models

# Create your models here.

class student(models.Model):
    Name=models.CharField(max_length=100)
    Mobile=models.IntegerField()
    Email=models.EmailField(max_length=100)
    Data_of_birth=models.DateField()
    Gender_choise=(
        ("male","Male"),
        ("female","Female"),
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
    )
    course=models.CharField(choices=Course_choise,max_length=100)
    father_name=models.CharField(max_length=100)
    mother_name=models.CharField(max_length=100)