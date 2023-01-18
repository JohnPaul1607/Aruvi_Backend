from django import forms
from .models import student



class RegisterStudent(forms.ModelForm):
    class Meta:
        model=student
        #fields=['name','mobile','email','date_of_birth','age','gender','academic_year','degree','course']
        fields='__all__'
    # widget={
    #     'Name':forms.CharField,
    #     'Mobile':forms.CharField,
    #     'Email':forms.CharField,
    #     'Date_of_birth':forms.DateField,
    #     'gender':forms.RadioSelect,
    #     'academic_year':forms.CharField,
    #     'degree':forms.CharField,
    #     'course':forms.Select,
        
    # }