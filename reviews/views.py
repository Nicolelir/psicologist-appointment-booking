from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import  CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Review
from .forms import ReviewForm

# Create your views here.

class BookingsPage(ListView):
    """View for displaying reviews"""
    model = Review
    template_name = 'reviews/reviews.html'  
    context_object_name = 'reviews' 

    # LoginRequiredMixin: only authenticated users can access a particular view. If a user is not authenticated, they will be redirected to the login page.
class AddBooking(LoginRequiredMixin, CreateView): 
    """Add review view"""

    template_name = "reviews/add_review.html"
    model = Review
    form_class = ReviewForm
    success_url = reverse_lazy("reviews")

    def form_valid(self, form):
        # Set the current user as the review user
        form.instance.user = self.request.user
        selected_date = form.cleaned_data.get('date')
        selected_time_str = form.cleaned_data.get('time')

"""
class ReviewList(generic.ListView):
    queryset = Review.objects.filter(status=1)
    template_name = "reviews/reviews.html"
    paginate_by = 6
"""
"""
def review_detail(request):
 
    queryset = Review.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    text = review.text.all().order_by("-created_on")
    text_count = review.text.filter(approved=True).count()
    if request.method == "POST":
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            text = review_form.save(commit=False)
            text.author = request.user
            text.post = post
            text.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Review submitted and awaiting approval'
            )
    
    review_form = ReviewForm()

    return render(
        request,
        "reviews/reviews.html",
        {
            "review": reviews,
            "text": text,
            "text_count": text_count,
            "review_form": review_form
        },
    )
"""

def reviews(request):
    return render(request, 'reviews/reviews.html')
