    
from django import forms
from .models import Teacher 
class TeacherForm(forms.Form):
        first_name = forms.CharField(max_length=10)
        last_name = forms.CharField(max_length=10)
        gender = forms.CharField(max_length=10)
        Registration = forms.CharField(max_length=10)
        Number = forms.CharField(max_length=10)
        City = forms.CharField(max_length=10)
        Age = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

        CHOICES = [
        ('Sélectionner une matière', 'Sélectionner une matière'),
        ('Mathématique', 'Mathématique'),
        ('EPS', 'EPS'),
        ('SVT', 'SVT'),
        ('Pysique', 'Pysique'),
        ('Chimie', 'Chimie'),
        ]
    
        Class = forms.ChoiceField(
            choices=CHOICES,
            widget=forms.Select(attrs={'class': 'form-group'})
        )

class TeacherFormu(forms.ModelForm):
    class Meta:
        model=Teacher
        fields=["first_name","last_name","gender","Class","Registration","Age","Number","City"]