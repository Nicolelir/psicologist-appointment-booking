from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    """A form to add a review"""

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['author'].initial = user.email  # Set initial value of the author field to user's email
        self.fields['author'].required = True
        self.fields['created_on'].required = True
        self.fields['service'].required = True
        self.fields['text'].required = True

        self.fields['author'].label = "Author"
        self.fields['created_on'].label = "Created on"
        self.fields['service'].label = "Service"
        self.fields['text'].label = "Text"

    class Meta:
        model = Review
        fields = ['author', 'created_on', 'service', 'text']


"""
class ReviewForm(forms.ModelForm):"""
"""Form for adding a review""""""
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
"""