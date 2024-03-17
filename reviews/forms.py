from django import forms
from django.contrib.auth.models import User
from django_summernote.widgets import SummernoteWidget
from django.contrib import messages
from .models import Review
from services.models import Services
from bookings.models import Booking

class ReviewForm(forms.ModelForm):
    """A form to add a review"""

    CHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )

    rating = forms.ChoiceField(
        choices=CHOICES, 
        required=True,
        label='Rate this therapist',
        help_text='Choose a rate 1 = Worst and 5 = Best',
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    service = forms.ModelChoiceField(queryset=Services.objects.all(), label='Service', widget=forms.Select(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Review
        fields = ['author', 'service', 'text', 'rating', ]  
    
        labels = {
            "author": "Published By",
            "service": "Service provided",
            "text":"Review",
            "rating":"Rating",
        }