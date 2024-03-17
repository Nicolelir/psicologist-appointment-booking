from django.urls import path
from .views import contact_form_view, home_view

app_name = 'home'

urlpatterns = [
    path('', home_view, name='home'),
    path('contact/', contact_form_view, name='contact_form'),

   
]