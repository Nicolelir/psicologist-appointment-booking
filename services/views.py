from django.shortcuts import render
from django.views.generic import ListView
from .models import About, Services



# Create your views here.
def about(request):
    """
    Renders the About section 
    """
    about = About.objects.all().order_by('-updated_on').first()
    print(about) 
    print(about.content)
    return render(
        request,
        "services/services.html",
        {"about": about},
    )

class ServicesListView(ListView):
    """View all services"""

    template_name = "services/services.html"
    queryset = Services.objects.all()
    context_object_name = "services"