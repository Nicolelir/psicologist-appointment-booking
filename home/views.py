from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm

def contact_form_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:contact_success')  # Redirect to a success page or home page
    else:
        form = ContactForm()

    return render(request, 'home/contact_form.html', {'form': form})

def contact_success_view(request):
    return render(request, 'home/contact_success.html')

def home_view(request):
    return render(request, 'home/index.html')  