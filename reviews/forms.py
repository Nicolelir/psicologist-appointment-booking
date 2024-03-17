from .models import Review
from django import forms

"""
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('text',)
"""

class ReviewForm(forms.ModelForm):
    """A form to add a review"""

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
          self.fields['email'].initial = user.email
        self.fields['author'].required = True
        self.fields['service'].required = True
        self.fields['text'].required = True
        self.fields['rating'].required = True
        self.fields['date'].required = True

        self.fields['author'].label = "Name"
        self.fields['service'].label = "Type of Service"
        self.fields['date'].widget = forms.DateInput(attrs={'type': 'date'})

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        time = cleaned_data.get('time')