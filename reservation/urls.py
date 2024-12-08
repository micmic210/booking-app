from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Home page
    path('philosophy/', views.philosophy_view, name='philosophy'),  # Philosophy page
    path('reservation/', views.reservation, name='reservation'),  # Reservation form
    path('confirmation/<str:reservation_number>/', views.confirmation, name='confirmation'),  # Confirmation
    path('cancel/', views.cancel_reservation, name='cancel_reservation'),  # Cancel reservation
]
