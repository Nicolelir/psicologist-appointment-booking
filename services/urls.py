from django.urls import path
from . import views
from .views import ServicesListView

urlpatterns = [
path('services/', ServicesListView.as_view(), name='services'),

]