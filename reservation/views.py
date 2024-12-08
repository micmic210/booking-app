from datetime import date
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import ReservationForm
from .models import Reservation


def index(request):
    """
    Renders the index page.
    """
    return render(request, "index.html")


def reservation(request):
    """
    Handles reservation form submission and rendering.
    """
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save()
            return redirect(
                "confirmation",
                reservation_number=reservation.reservation_number,
            )
    else:
        form = ReservationForm()

    # Pass today's date as ISO-8601 formatted string (YYYY-MM-DD)
    today_date = date.today().isoformat()

    return render(
        request,
        "reservation/reservation.html",
        {"form": form, "today_date": today_date},
    )


def philosophy_view(request):
    """
    Renders the philosophy page.
    """
    return render(request, "philosophy.html")


def thank_you_view(request):
    """
    Renders the thank-you page for contact form submission.
    """
    return render(request, "contact/thank_you.html")


def confirmation(request, reservation_number):
    """
    Displays the confirmation page with reservation details.
    """
    reservation = get_object_or_404(
        Reservation,
        reservation_number=reservation_number,
    )
    return render(
        request,
        "reservation/confirmation.html",
        {"reservation": reservation},
    )


def cancel_reservation(request):
    """
    Simplified reservation cancellation logic.
    """
    if request.method == "POST":
        reservation_number = request.POST.get("reservation_number")

        try:
            # Find the reservation by number
            reservation = Reservation.objects.get(
                reservation_number=reservation_number,
            )

            # Delete the reservation
            reservation.delete()
            messages.success(
                request,
                "Your reservation has been successfully canceled.",
            )
        except Reservation.DoesNotExist:
            # If reservation not found, display a warning message
            messages.warning(
                request,
                "Reservation number not found. Please check and try again.",
            )

        # Redirect to the cancellation page
        return redirect("cancel_reservation")

    return render(request, "reservation/cancellation.html")
