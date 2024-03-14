from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Booking

class BookingForm(forms.ModelForm):
    """A form to add a booking"""

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['email'].initial = user.email
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['date'].required = True

        self.fields['first_name'].label = "First Name"
        self.fields['last_name'].label = "Last Name"
        
        self.fields['date'].widget = forms.DateInput(attrs={'type': 'date'})

    

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