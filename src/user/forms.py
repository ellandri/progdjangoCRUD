    
from django import forms
from .models import User

class UserForm(forms.Form):
        Pseudo = forms.CharField(max_length=10)
        Mot_de_passe = forms.CharField(max_length=100)

class UserFormu(forms.ModelForm):
        class Meta:
                model = User
                fields = ["Pseudo", "Mot_de_passe",]
  #              fields = "__all__"
  #              exclude = ("creat_at",)