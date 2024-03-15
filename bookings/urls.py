from django.urls import path
from . import views


urlpatterns = [
    path("", views.BookingsPage.as_view(), name='bookings'),
    path('add/', views.AddBooking.as_view(), name='booking_add'),
    path('edit/<int:pk>/', views.EditBooking.as_view(), name='edit_booking'),
    path('delete/<int:pk>/',views.DeleteBooking.as_view(), name='delete_booking'),
    
]