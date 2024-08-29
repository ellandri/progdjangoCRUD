from django.urls import path
from dashboard.views import index
from . import views
app_name='report'
urlpatterns = [
   path('report/', views.report_view, name='report'),
    
    
]