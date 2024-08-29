from django.shortcuts import render,redirect
from .models import Teacher
from .forms import TeacherForm, TeacherFormu

# Create your views here.
def teacher(request):
    teachers = Teacher.objects.all()  
    
    form = TeacherForm()
    return render(request, 'teacher/teacher.html',{'teachers':teachers})

def add_teacher(request):
    if request.method == "POST":
        teacher_formu=TeacherFormu(request.POST)
        if teacher_formu.is_valid():
            
            print(teacher_formu.cleaned_data)
            teacher_formu.save()
            print(request.POST)
    form = TeacherForm()
    return render(request, 'teacher/add_teacher.html', {'form': form})

def edit_teacher(request, id):
    #student = get_object_or_404(Student, id=id)
    teacher =  Teacher.objects.get(id=id)
    if request.method=="POST":
        teacher_form = TeacherFormu(request.POST, instance=teacher)
        
        if teacher_form.is_valid():
            teacher_form.save()
            return redirect('teacher:index')
    
    teacher_form = TeacherFormu(instance=teacher)
    
    #context["student_form"]=student_form
    return render(request, 'teacher/edit_teacher.html',{"teacher_form":teacher_form} )

def delete_teacher(request,id):
    teacher =  Teacher.objects.get(id=id)
    teacher.delete()
    return redirect("teacher:index")