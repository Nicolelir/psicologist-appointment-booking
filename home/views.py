from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm 
from .models import Contact

def contact_form_view(request):
    message_sent = False  # Initialize the success message flag
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # Set the success message flag to True
            message_sent = True
    else:
        form = ContactForm() 

    return render(request, 'home/index.html', {'form': form, 'message_sent': message_sent})

def home_view(request):
    message_sent = False  # Initialize the success message flag

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # Set the success message flag to True
            message_sent = True
            messages.success(request, "Your message has been sent successfully!")
    else:
        form = ContactForm()

    if not request.user.is_authenticated:
        # User is not authenticated, display the message
        message = "Invest in Yourself: Book a Session with Elvira, Your Trusted Mentor!"
    else:
        # User is authenticated, do not display the message
        message = None

    return render(request, 'home/index.html', {'form': form, 'message': message, 'message_sent': message_sent})