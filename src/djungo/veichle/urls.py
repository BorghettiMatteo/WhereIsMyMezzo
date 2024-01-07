from django import views
from django.urls import path
from src.djungo.veichle.views import VeichleView

urlpatterns = [
    path("", VeichleView.as_view())
]