from django import forms
from .models import Review, Booking, Services
class ReviewForm(forms.ModelForm):
    """A form to add a review"""

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)


        if user:
            self.fields['booking'].queryset = Booking.objects.filter(user=user)
            
    
        # Exclude author field manually
        self.fields.pop('author', None)

    def clean_author(self):
        author = self.cleaned_data.get('author')
        if not author:
            raise forms.ValidationError("Author field is required.")
        return author

    class Meta:
        model = Review
        fields = ['created_on', 'booking', 'service', 'rating', 'text']
