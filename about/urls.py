from . import views
from django.urls import path

urlpatterns = [
    path("about/", views.get_content, name="about"),
]
