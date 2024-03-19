from django import forms
from .models import Review, Booking

class ReviewForm(forms.ModelForm):
    """A form to add a review"""

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            self.fields['author'].initial = user
            self.fields['author'].queryset = Review.objects.filter(author=user)
            self.fields['booking'].queryset = Booking.objects.filter(user=user)
            self.fields['author'].required = True
            self.fields['created_on'].required = True
            self.fields['service'].required = True
            self.fields['booking'].required = True
            self.fields['rating'].required = True
            self.fields['text'].required = True

            self.fields['author'].label = "Author"
            self.fields['created_on'].label = "Created on"
            self.fields['booking'].label = "Booking"
            self.fields['service'].label = "Service"
            self.fields['rating'].label = "Rating"
            self.fields['text'].label = "Text"

    def save(self, commit=True):
        instance = super().save(commit=False)
        if not instance.author_id:
            instance.author = self.initial['author']
        if commit:
            instance.save()
        return instance

    class Meta:
        model = Review
        fields = ['author', 'created_on', 'booking', 'service', 'rating', 'text']