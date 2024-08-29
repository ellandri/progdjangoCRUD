    
from django import forms
from .models import Student  # Assurez-vous que cela correspond à votre fichier models.py

class StudentForm(forms.Form):
        first_name = forms.CharField(max_length=10)
        last_name = forms.CharField(max_length=10)
        gender = forms.CharField(max_length=10)
        Registration = forms.CharField(max_length=10)
        Number = forms.CharField(max_length=10)
        City = forms.CharField(max_length=10)
        Age = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

        CHOICES = [
        ('Tle', 'Tle'),
        ('1ere', '1ere'),
        ('2nd', '2nd'),
        ('3ème', '3ème'),
        ('4ème', '4ème'),
        ('5ème', '5ème'),
        ('6ème', '6ème'),
        ]
        
        Class = forms.ChoiceField(
            choices=CHOICES,
            widget=forms.Select(attrs={'Class': 'form-group'})
        )
class StudentFormu(forms.ModelForm):
    
    class Meta:
        model=Student
        fields=["first_name","last_name","gender","Class","Registration","Age","Number","City"]