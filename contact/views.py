from django.shortcuts import render

def contact_view(request):
    return render(request, 'contact/contact.html')

def thank_you_view(request):
    return render(request, 'contact/thank_you.html')

