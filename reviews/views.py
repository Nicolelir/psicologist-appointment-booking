from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from django.views import generic, View
from django.contrib.messages.views import SuccessMessageMixin
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for review in context['reviews']:
            review.full_stars = range(review.rating)
            review.empty_stars = range(5 - review.rating)
        return context
        
    # Ensure that the method is indented properly within the class

class AddReview(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    A model to create a review
    """
    template_name = 'reviews/add_review.html'
    model = Review
    form_class = ReviewForm
    success_url = reverse_lazy('reviews')  # Use reverse_lazy for success_url
    success_message = "Review added successfully."

    def form_valid(self, form):
        # Set the author of the review to the current user
        form.instance.author = self.request.user
        # Save the review instance
        response = super().form_valid(form)
        # Display success message
        messages.success(self.request, 'Review added successfully.')
        return response

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  # Pass the current user to the form
        return kwargs

class ReviewList(generic.ListView):
    """
    A model to view the review cards, no more than 8 to a page
    """
    model = Review
    template_name = 'reviews/reviews.html'
    paginate_by = 8