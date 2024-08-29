from django.shortcuts import render, redirect
from .forms import  UserForm,UserFormu
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def user(request):
    users = User.objects.all()  # Récupère tous les utilisateurs
    return render(request, 'user/index.html', {'users': users})

def edit_user(request, id):
    #student = get_object_or_404(Student, id=id)
    user =  User.objects.get(id=id)
    if request.method=="POST":
        user_form = UserFormu(request.POST, instance=user)
        
        if user_form.is_valid():
            user_form.save()
            return redirect('user:index')
    
    user_form = UserFormu(instance=user)
    
    #context["student_form"]=student_form
    return render(request, 'user/edit_user.html',{"user_form":user_form} )


def add_user(request):
    if request.method == "POST":
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        
        if not username or not password:
            return render(request,'user/add_user.html')
        user = User(username=username)
        user.save()
        user.password = password
        user.set_password(user.password)
        user.save()
        
        return redirect('user:add')
    return render(request,'user/add_user.html')
        
        

