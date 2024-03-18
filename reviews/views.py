from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse
from .forms import ReviewForm
from .models import Review


class ReviewPage(ListView):
    """View for displaying reviews"""
    model = Review
    template_name = 'reviews/reviews.html'  
    context_object_name = 'reviews' 

class AddReview(CreateView):
    """
    A view to create a review
    """
    template_name = 'reviews/add_review.html'
    model = Review
    form_class = ReviewForm
    success_url = reverse_lazy('reviews')  # Use reverse_lazy for success_url

    def form_valid(self, form):
        # Set the author of the review to the current user
        form.instance.author = self.request.user
        # Save the review instance
        response = super().form_valid(form)
        # Display success message
        messages.success(self.request, 'Review added successfully.')
        return response