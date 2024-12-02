from django import forms
from .models import Reservation


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'email', 'phone', 'reservation_date', 'reservation_time', 'guests']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your full name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email address'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'}),
            'reservation_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'reservation_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'guests': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Guests'}),
        }
