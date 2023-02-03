from django.urls import path, include

from . import views

urlpatterns = [
    path('artists/', views.ArtistListView.as_view()),
    path('artists/<int:pk>/', views.ArtistDetailView.as_view()),
]
