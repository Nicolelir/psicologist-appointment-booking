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
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect('home:home')  # Redirect to the home page to clear the form
    else:
        form = ContactForm()

    return render(request, 'home/index.html', {'form': form})

   