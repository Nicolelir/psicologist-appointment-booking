from django.contrib import messages
from django.urls import reverse_lazy
from django.utils import timezone
from datetime import datetime
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Booking
from .forms import BookingForm


class BookingsPage(ListView):
    """View for displaying bookings"""
    model = Booking
    template_name = 'bookings/bookings.html'  
    context_object_name = 'bookings' 

class AddBooking(LoginRequiredMixin, CreateView):
    """Add booking view"""

    template_name = "bookings/add_booking.html"
    model = Booking
    form_class = BookingForm
    success_url = reverse_lazy("bookings")

    def form_valid(self, form):
        # Set the current user as the booking user
        form.instance.user = self.request.user
        selected_date = form.cleaned_data.get('date')
        selected_time_str = form.cleaned_data.get('time')

        # Get the current date and time
        current_datetime = timezone.now()

        # Check if date is in the past
        if (selected_date < current_datetime.date() or
            (selected_date == current_datetime.date() and
            datetime.strptime(selected_time_str.split(' - ')[0], '%H:%M').time() < current_datetime.time())):
            form.add_error('date', 'Please enter a valid date')
            return self.form_invalid(form)

        messages.success(self.request, "Thanks for booking an appointment")
        return super().form_valid(form)