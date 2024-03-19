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
    return render(request, 'includes/footer.html', {'form': form})

def home_view(request):
   
    return render(request, 'home/index.html')