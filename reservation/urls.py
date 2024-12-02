from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('philosophy/', views.philosophy_view, name='philosophy'),  
    path('reservation/', views.reservation, name='reservation'),
    path('confirmation/<str:reservation_number>/', views.confirmation, name='confirmation'),  
]
