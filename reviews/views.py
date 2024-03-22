from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, ListView, DetailView
from django.urls import reverse_lazy
from django.views import generic, View
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.contrib import messages
from django.urls import reverse
from .forms import ReviewForm
from .models import Review
from .models import Booking

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
        
  
@login_required
def add_review(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    if booking.user != request.user:
        # User is not authorized to leave a review for this booking
        return redirect('home')  # Redirect to home page or appropriate URL

    if request.method == 'POST':
        form = ReviewForm(request.POST, user=request.user)  # Pass the user parameter to the form
        if form.is_valid():
            review = form.save(commit=False)
            review.booking = booking
            review.author = request.user
            review.save()
            return redirect('bookings', booking_id=booking_id)  # Redirect to booking detail page
    else:
        form = ReviewForm(user=request.user)  # Pass the user parameter to the form
    return render(request, 'add_review.html', {'form': form})


class AddReview(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    A model to create a review
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

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  # Pass the current user to the form
        return kwargs

class ReviewList(generic.ListView):
    """
    A model to view the review cards, no more than 6 to a page
    """
    model = Review
    template_name = 'reviews/reviews.html'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = context['object_list']  # Set 'reviews' to the paginated queryset
        return context

class ReviewDetail(DetailView):
    """View a single review"""

    template_name = "reviews/review_detail.html"
    model = Review
    context_object_name = "review"