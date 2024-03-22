from django.urls import path
from . import views

urlpatterns = [
    path("", views.ReviewPage.as_view(), name='reviews'),
    path('add/', views.AddReview.as_view(), name='review_add'),
    path('review/<int:pk>/', views.ReviewDetail.as_view(), name='review_detail'),

    
]