from django.urls import path 
from .views import TestView
urlpatterns = [
    path('paycom/', TestView.as_view())
]