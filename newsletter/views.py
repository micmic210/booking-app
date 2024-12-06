from django.shortcuts import render, redirect
from .forms import SubscriptionForm
from django.contrib import messages
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os

def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            subscriber = form.save()
            
            # Send confirmation email
            send_confirmation_email(subscriber.email)
            
            messages.success(request, 'Subscription successful! Please check your email for confirmation.')
            return redirect('subscribe')
        else:
            messages.error(request, 'Invalid email address. Please try again.')
    
    else:
        form = SubscriptionForm()
    
    return render(request, 'newsletter/subscribe.html', {'form': form})

def send_confirmation_email(email):
    message = Mail(
        from_email='your-email@example.com',
        to_emails=email,
        subject='Thank you for subscribing!',
        html_content='<p>Thank you for subscribing to our newsletter!</p>'
    )
    try:
        sg = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))
        sg.send(message)
    except Exception as e:
        print(e.message)
