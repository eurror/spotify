from django.urls import path, include

from . import views

urlpatterns = [
    path('songs/', views.SongListView.as_view()),
    path('songs/<int:pk>/', views.SongDetailView.as_view()),
]
