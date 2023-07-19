from django.urls import path

from .views import LibraryView, LibraryDetailView

urlpatterns = [
    path("libs/", LibraryView.as_view()),
    path("libs/<int:pk>/", LibraryDetailView.as_view()),
]