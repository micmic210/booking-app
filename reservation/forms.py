from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import time
from .models import Reservation
import re


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'email', 'phone', 'reservation_date', 'reservation_time', 'guests']
        widgets = {
            'name': forms.TextInput(attrs={'id': 'name', 'class': 'form-control', 'placeholder': 'Enter your full name'}),
            'email': forms.EmailInput(attrs={'id': 'email', 'class': 'form-control', 'placeholder': 'Enter your email'}),
            'phone': forms.TextInput(attrs={'id': 'phone', 'class': 'form-control', 'placeholder': 'Enter your phone number'}),
            'reservation_date': forms.DateInput(attrs={'id': 'reservation_date', 'class': 'form-control', 'type': 'date'}),
            'reservation_time': forms.TimeInput(attrs={'id': 'reservation_time', 'class': 'form-control', 'type': 'time'}),
            'guests': forms.NumberInput(attrs={'id': 'guests', 'class': 'form-control', 'placeholder': 'Number of Guests'}),
        }

    def clean_name(self):
        name = self.cleaned_data.get("name", "").strip()
        if not name:
            raise ValidationError("Name is required.")
        return name

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if email is None or email.strip() == "":
            raise ValidationError("Email is required.")
        return email.strip()

    def clean_phone(self):
        phone = self.cleaned_data.get("phone", "").strip()
        if not phone:
            raise ValidationError("Phone number is required.")
        if not re.match(r'^\+?\d{10,15}$', phone):
            raise ValidationError("Enter a valid phone number (digits only).")
        return phone

    def clean_guests(self):
        guests = self.cleaned_data.get("guests")

        if guests is None:
            raise ValidationError("Number of guests is required.")

        if not isinstance(guests, int) or guests <= 0:
            raise ValidationError("Number of guests must be a positive integer.")

        return guests

    def clean(self):
        cleaned_data = super().clean()
        reservation_date = cleaned_data.get("reservation_date")
        reservation_time = cleaned_data.get("reservation_time")

        if not reservation_date:
            self.add_error("reservation_date", "Reservation date is required.")

        if not reservation_time:
            self.add_error("reservation_time", "Reservation time is required.")

        try:
            reservation_datetime = timezone.make_aware(
                timezone.datetime.combine(reservation_date, reservation_time),
                timezone.get_current_timezone()
            )
        except Exception as e:
            self.add_error("reservation_date", "Invalid reservation date and time.")
            return cleaned_data

        if reservation_datetime < timezone.now():
            # Associate the error with the `reservation_date` field
            self.add_error("reservation_date", "The reservation date and time cannot be in the past. Please select a future date and time.")

        return cleaned_data

    def clean_reservation_time(self):
        reservation_time = self.cleaned_data.get("reservation_time")
        if not reservation_time:
            raise ValidationError("Reservation time is required.")

        # Compare using datetime.time
        if reservation_time < time(12, 0) or reservation_time > time(21, 0):
            raise ValidationError("Reservation time must be between 12:00 and 21:00.")
        return reservation_time
