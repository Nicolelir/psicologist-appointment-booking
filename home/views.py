from django.shortcuts import render, redirect
from .forms import FooterForm 
from .models import Contact


def contact_form_view(request):
    if request.method == 'POST':
        form = FooterForm(request.POST)  
        
        if form.is_valid():
            # Save the form data to the database using Contact model
            Contact.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                query=form.cleaned_data['query']
            )
            return redirect('home:home')
    else:
        form = FooterForm() 
    return render(request, 'includes/footer.html', {'form': form})

def home_view(request):

    form = FooterForm()
    return render(request, 'home/index.html')