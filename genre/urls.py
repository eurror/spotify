from django.urls import path, include

from . import views

urlpatterns = [
    path('genres/', views.GenreListView.as_view()),
    path('genres/<int:pk>/', views.GenreDetailView.as_view()),
]
