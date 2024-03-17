from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse
from .forms import ReviewForm
from .models import Review

def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            # Extract the service ID from the form data
            service_id = form.cleaned_data['service'].id
            # Get the service object using the extracted ID
            service = get_object_or_404(Services, id=service_id)
            # Set the service field of the review object
            review.services = service
            review.save()
            messages.success(request, 'Review added successfully.')
            return redirect('reviews')  # Redirect to the reviews page after adding the review
    else:
        form = ReviewForm()
    return render(request, 'add_review.html', {'form': form})

# Ensure that the form is passed to the template context
    assert form is not None, "Form instance is None"

def reviews(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user  # Assign the current user as the author
            form.save()
            return redirect('reviews')
    else:
        form = ReviewForm()

    reviews = Review.objects.all()
    return render(request, 'reviews/reviews.html', {'reviews': reviews, 'form': form})

class AddReview(LoginRequiredMixin, CreateView):
    """
    A view to create a review
    """
    template_name = 'reviews/add_review.html'
    model = Review
    form_class = ReviewForm
    success_url = 'reviews'

    def form_valid(self, form):
        form.instance.author = self.request.user

        # save the review instance
        response = super().form_valid(form)

        # check if the review is approved or awaiting approval
        if form.instance.status == 0:
            messages.info(self.request, 'Your review is awaiting approval.')

        return response

    def get_success_url(self):
        # Redirect to the list of reviews after successful creation
        return reverse('reviews')  # Replace 'reviews' with the actual URL name