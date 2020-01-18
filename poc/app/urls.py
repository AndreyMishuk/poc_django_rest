from app import views
from django.urls import path


urlpatterns = [
    path('hello', views.HomeView.as_view()),
]

