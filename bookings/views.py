from django.contrib import messages
from django.urls import reverse_lazy
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Booking
from .forms import BookingForm



class BookingsPage(ListView):
    """View for displaying bookings"""
    model = Booking
    template_name = 'bookings/bookings.html'  
    context_object_name = 'bookings' 

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings.html', {'bookings': bookings})

# LoginRequiredMixin: only authenticated users can access a particular view. If a user is not authenticated, they will be redirected to the login page.
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

        messages.success(self.request, "Thank you for booking an appointment with me! Don't forget to leave a review after your session")
        return super().form_valid(form)

# UserPassesTestMixin:This mixin allows to define custom permission checks for a view. 
class EditBooking(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Edit a booking
    """
    model = Booking
    form_class = BookingForm
    template_name = 'bookings/edit_booking.html'
    success_url = reverse_lazy('bookings')

    def test_func(self):
        booking = self.get_object()
        return self.request.user == booking.user

    def form_valid(self, form):
        form.instance.user = self.request.user

         # Exclude date and time fields from cleaned data - credit Django docs
        cleaned_data = form.cleaned_data
        new_date = cleaned_data.get('date')
        new_time = cleaned_data.get('time')

        # Check if the new time and date are available
        if new_date and new_time:
            existing_booking = Booking.objects.filter(
                date=new_date,
                time=new_time).exclude(pk=self.object.pk).first()
            if existing_booking:
                form.add_error('time', 'This time and date is already booked, Please select another time and date')
                return self.form_invalid(form)

        messages.success(self.request, "Your booking has been updated.")

        return super().form_valid(form)

class DeleteBooking(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Delete a  Booking
    """
    model = Booking
    template_name = 'bookings/delete_booking.html'
    success_url = reverse_lazy('bookings')

    def test_func(self):
        booking = self.get_object()
        return self.request.user == booking.user

    def delete(self, request, *args, **kwargs):
        # Display success message
        messages.success(self.request, "Your booking has been deleted.")

        return super().delete(request, *args, **kwargs)


