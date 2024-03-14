from django.urls import path
from . import views


urlpatterns = [
    path("", views.BookingsPage.as_view(), name='bookings'),
    path('add/', views.AddBooking.as_view(), name='booking_add'),
    
]