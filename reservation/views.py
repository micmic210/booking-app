from django.shortcuts import render, get_object_or_404, redirect
from .forms import ReservationForm
from .models import Reservation
from django.contrib import messages


def index(request):
    """
    Renders the index page.
    """
    return render(request, 'index.html')


def reservation(request):
    """
    Handles reservation form submission and rendering.
    """
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save()
            return redirect(
                'confirmation',
                reservation_number=reservation.reservation_number
            )
    else:
        form = ReservationForm()

    return render(
        request,
        'reservation/reservation.html',
        {'form': form}
    )


def philosophy_view(request):
    """
    Renders the philosophy page.
    """
    return render(request, 'philosophy.html')


def thank_you_view(request):
    """
    Renders the thank-you page for contact form submission.
    """
    return render(request, 'contact/thank_you.html')


def confirmation(request, reservation_number):
    """
    Displays the confirmation page with reservation details.
    """
    reservation = get_object_or_404(
        Reservation,
        reservation_number=reservation_number
    )
    return render(
        request,
        'reservation/confirmation.html',
        {'reservation': reservation}
    )


def cancel_reservation(request):
    """
    Handles reservation cancellation logic.
    """
    if request.method == "POST":
        reservation_number = request.POST.get("reservation_number")
        name = request.POST.get("name", "").strip()

        try:
            # Try to find the reservation
            reservation = Reservation.objects.get(
                reservation_number=reservation_number,
                name=name
            )

            if request.POST.get("confirm_cancel") == "true":
                reservation.delete()
                messages.success(
                    request,
                    "Your reservation has been successfully canceled."
                )
                return redirect("cancel_reservation")

            # If not confirmed, display for confirmation
            return render(
                request,
                "reservation/cancellation.html",
                {
                    "reservation": reservation,
                    "show_cancel_button": True
                }
            )

        except Reservation.DoesNotExist:
            # Reservation not found
            messages.warning(
                request,
                "Reservation not found. Please check your reservation number "
                "and name."
            )

    return render(
        request,
        "reservation/cancellation.html",
        {"show_cancel_button": False}
    )
