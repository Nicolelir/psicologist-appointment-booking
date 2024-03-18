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


class AddReview(LoginRequiredMixin, CreateView):
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
        # Check if the review is approved or awaiting approval
        if form.instance.status == 0:
            messages.info(self.request, 'Your review is awaiting approval.')
        else:
            messages.success(self.request, 'Review added successfully.')
        return response

    def get_form_kwargs(self):
        # Pass the request user to the form
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

def reviews(request):
    reviews = Review.objects.all()
    return render(request, 'reviews/reviews.html', {'reviews': reviews})

def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.save()
            return redirect('reviews')  # Redirect to the reviews page after adding the review
    else:
        form = ReviewForm()
    return render(request, 'add_review.html', {'form': form})
