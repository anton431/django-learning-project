from django.urls import path

from . import views


urlpatterns = [
    path('', views.MociesView.as_view()),
    path("<slug:slug>/", views.MovieDetailView.as_view(), name="movie_detail"),
    path("reviw/<int:pk>/", views.AddReview.as_view(), name="add_review"),
    path("actors/<str:slug>/", views.ActorView.as_view(), name="actor_detail"),
]