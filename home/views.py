from django.shortcuts import render, redirect
from .forms import ContactForm 
from .models import Contact

def contact_form_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)  
        if form.is_valid():
            form.save()
            return redirect('home:home')
    else:
        form = ContactForm() 
    return render(request, 'home/contact_form.html', {'form': form})

def home_view(request):
    if request.method != 'POST':
        form = ContactForm()  # Include the form only for GET requests
    else:
        form = None  # No need to include the form for POST requests
    return render(request, 'home/index.html', {'form': form})