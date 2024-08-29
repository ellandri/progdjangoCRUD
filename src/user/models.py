from django.db import models
from django import forms

# Create your models here.
class User(models.Model):
    Pseudo = models.CharField(max_length=10, unique=True, default='aka0102')
    Mot_de_passe = models.CharField(max_length=100, default="azerty")
    Creat_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Mot_de_passe
    class Meta:
        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"

class UserSecond(models.Model):
    Pseudo = models.CharField(max_length=10, unique=True, default='aka0102')
    Mot_de_passe = models.CharField(max_length=100, default="azerty")
    #Creat_date = models.DateTimeField(auto_now_add=True)