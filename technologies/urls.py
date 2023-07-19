from django.urls import path

from .views import TechnologyView, TechnologyDetailView

urlpatterns = [
    path("technology/", TechnologyView.as_view()),
    path("technology/<int:pk>/", TechnologyDetailView.as_view()),
]