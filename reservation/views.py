from django.shortcuts import render, get_object_or_404, redirect
from .forms import ReservationForm
from .models import Reservation

# Create your views here.

def index(request):
    """
    Renders the index page.
    """

    return render(request, 'index.html')


def reservation(request):
    """
    Handles reservation form submissin and rendering.
    """

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save()  # Save the reservation
            return redirect('confirmation', reservation_number=reservation.reservation_number)
    else:
        form = ReservationForm()
    
    return render(request, 'reservation/reservation.html', {'form': form})


def philosophy_view(request):
    """
    Renders the philosophy page.
    """
    return render(request, 'philosophy.html')


def thank_you_view(request):
    """
    Renders the thank you page for contact form submission.
    """

    return render(request, 'contact/thank_you.html')


def confirmation(request, reservation_number):
    """
    Displays the confirmation page with reservation details.
    """
    reservation = get_object_or_404(Reservation, reservation_number=reservation_number)
    return render(request, 'reservation/confirmation.html', {'reservation': reservation})
