from django.urls import path
from dashboard.views import index
from . import views

app_name='user'
urlpatterns = [
   path('user/', views.user, name='index'),
    path('addu/', views.add_user, name='add'),
    path('editu/<int:id>/', views.edit_user, name='edit'),
]

