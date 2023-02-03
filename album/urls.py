from django.urls import path, include

from . import views

urlpatterns = [
    path('albums/', views.AlbumListView.as_view()),
    path('albums/<int:pk>/', views.AlbumDetailView.as_view()),
]
