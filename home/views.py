from django.shortcuts import render, redirect
from .forms import FooterForm 
from .models import Contact


def contact_form_view(request):
    if request.method == 'POST':
        footer_form = FooterForm(request.POST)  
        
        if footer_form.is_valid():
            # Save the form data to the database using Contact model
            Contact.objects.create(
                name=footer_form.cleaned_data['name'],
                email=footer_form.cleaned_data['email'],
                query=footer_form.cleaned_data['message']
            )
            return redirect('home')
    else:
        footer_form = FooterForm() 

    return render(request, 'includes/footer.html', {'footer_form': footer_form})

def home_view(request):
    return render(request, 'home/index.html')