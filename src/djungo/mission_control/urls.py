from django import views
from django.urls import path
from src.djungo.mission_control.views import MissionControlView

urlpatterns = [
    path("", MissionControlView.as_view())
]