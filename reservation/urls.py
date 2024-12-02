from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('philosophy/', views.philosophy_view, name='philosophy'),  
    path('reservation/', views.reservation, name='reservation'),
    path('thank_you/', views.thank_you_view, name='thank_you'),
]
