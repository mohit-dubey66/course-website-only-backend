from django import views
from django.urls import path
from course.views import home

urlpatterns = [
    path("", home, name='home'),
]