from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')


def reservation(request):
    """
    Handles the reservation page request.
    Renders the reservation.html template.
    """
    context = {
        "page_title": "Reservation",  # Example of data to pass to the template
    }
    return render(request, 'reservation/reservation.html', context)


def philosophy_view(request):
    return render(request, 'philosophy.html')


def thank_you_view(request):
    return render(request, 'contact/thank_you.html')

