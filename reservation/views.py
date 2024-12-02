from django.shortcuts import render

# Create your views here.

def reservation(request):
    """
    Handles the reservation page request.
    Renders the reservation.html template.
    """
    context = {
        "page_title": "Reservation",  # Example of data to pass to the template
    }
    return render(request, 'reservation/reservation.html', context)
