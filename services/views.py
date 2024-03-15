from django.shortcuts import render
from django.views.generic import ListView
from .models import Services



# Create your views here.

class ServicesListView(ListView):
    """View all services"""

    template_name = "services/services.html"
    queryset = Services.objects.all()
    context_object_name = "services"