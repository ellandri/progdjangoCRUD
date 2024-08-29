from django.urls import path
from dashboard.views import index
from . import views
app_name='dashboard'
urlpatterns = [
   path('dashbord', views.index, name='index'),
    path('', views.connect_view, name='connect'),

    
]