from django.urls import path
from dashboard.views import index
from . import views


app_name = 'student'

urlpatterns = [
   path('student/', views.student, name='index'),
   path('adds/', views.add_student, name='add'),
    path('edit/<int:id>/', views.edit_student, name='edit'),
    path('delete/<int:id>/', views.delete_student, name='delete'),
    
    
]