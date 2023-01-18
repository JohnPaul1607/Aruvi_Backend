from django import forms
from .models import student


class RegisterStudent(forms.ModelForm):
    class Meta:
        model=student
        fields="__all__"
    widget={
        'Name':forms.TextInput(attrs={'class':'form-control','placeholder':'Ex: John'}),
        'Mobile':forms.NumberInput(attrs={'class':'form-control','placeholder':'Ex: 9876543210'}),
        'Email':forms.TextInput(attrs={'class':'form-control','placeholder':'Ex: john@gmail.com'}),
        'Date_of_birth':forms.DateInput(attrs={'class':'form-control','placeholder':'Ex: 16/07/2000'}),
        'gender':forms.RadioSelect(attrs={'class':'form-control'}),
        'academic_year':forms.TextInput(attrs={'class':'form-control','placeholder':'Ex: 2021'}),
        'degree':forms.TextInput(attrs={'class':'form-control','placeholder':'Ex: BE'}),
        'course':forms.Select(attrs={'class':'form-control'}),
        
    }