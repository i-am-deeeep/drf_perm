from django.urls import path
from . import views

urlpatterns = [
    path("movielist/", views.MovieListAV.as_view()),
    path("movie/<int:pk>", views.MovieDetailAV.as_view()),
    path("reviewlist/", views.ReviewListAV.as_view()),
    path("review/<int:pk>", views.ReviewDetailAV.as_view()),
]