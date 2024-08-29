from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm, StudentFormu
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def student(request):
    students = Student.objects.all()  
    return render(request, 'student/index.html',{'students':students})

def add_student(request):
    if request.method == "POST":
        
        print(request.POST)
        student_formu=StudentFormu(request.POST)
        
        if student_formu.is_valid():
            
            print(student_formu.cleaned_data)
            student_formu.save()
            
            print(request.POST)
            
    form = StudentForm()
            
    return render(request, 'student/add.html', {'form': form})

def edit_student(request, id):
    #student = get_object_or_404(Student, id=id)
    student =  Student.objects.get(id=id)
    if request.method=="POST":
        student_form = StudentFormu(request.POST, instance=student)
        
        if student_form.is_valid():
            student_form.save()
            return redirect('student:index')
    
    student_form = StudentFormu(instance=student)
    
    #context["student_form"]=student_form
    return render(request, 'student/edit.html',{"student_form":student_form} )

def delete_student(request,id):
    student =  Student.objects.get(id=id)
    student.delete()
    return redirect("student:index")
