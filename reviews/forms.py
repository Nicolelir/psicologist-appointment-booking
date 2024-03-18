from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    """Form for adding a review"""
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
        label='Rate this movie',
        help_text='Choose a rate 1 = Worst and 5 = Best'
    )
    class Meta:
        model = Review
        fields = ['service', 'rating', 'text']