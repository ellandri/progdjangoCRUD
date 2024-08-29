from django.urls import path
from dashboard.views import index
from . import views
app_name='teacher'
urlpatterns = [
    path('teacher/', views.teacher, name='index'),
    path('addt/', views.add_teacher, name='add'),
    path('editt/<int:id>/', views.edit_teacher, name='edit'),
    path('deletet/<int:id>/', views.delete_teacher, name='delete'),

]