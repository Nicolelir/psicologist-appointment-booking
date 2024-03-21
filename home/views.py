from django.shortcuts import render, redirect
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
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # If the form is valid and saved, redirect to the same page to refresh the form
            return redirect('home:home')
    else:
        form = ContactForm()  # Assign the form here for GET requests

    return render(request, 'home/index.html', {'form': form})