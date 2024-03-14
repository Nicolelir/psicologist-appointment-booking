from django.urls import path
from . import views
from .views import About, ServicesListView

urlpatterns = [
path('', views.about, name='about'),
path('services/', ServicesListView.as_view(), name='services'),

]