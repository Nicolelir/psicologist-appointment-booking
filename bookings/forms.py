from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Booking

class BookingForm(forms.ModelForm):
    """A form to add a booking"""

    
    class Meta:
        model = Booking
        fields = [
            'first_name', 'last_name', 'email', 'date', 'time', 'notes',
        ]
     
    notes = forms.CharField(widget=RichTextWidget())

    labels = {
            "user": "Booking By",
            "first_name":"First Name",
            "last_name":"Last Name",
            "email":"Email",
            "date":"Booking Date",
            "time":"Booking Time",
            "notes": "Notes",
        }