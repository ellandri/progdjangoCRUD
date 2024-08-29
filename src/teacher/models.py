from django.db import models
from django import forms

# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=30, default='Féminin')
    Class = models.CharField(max_length=30, default='Non-spécifiée')
    Registration = models.CharField(max_length=30, default='01D022526')
    Age = models.CharField(max_length=30, null=False, default='2000/10/01')
    Number = models.CharField(max_length=30, default='00000000')
    City = models.CharField(max_length=30, default='Non-spécifiée')

    CHOICES = [
        ('option1', 'Sélectionner une matière'),
        ('option2', 'Mathématique'),
        ('option3', 'Français'),

        ]
    
    choix = forms.ChoiceField(
            choices=CHOICES,
            widget=forms.Select(attrs={'class': 'form-group'})
        )
