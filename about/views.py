from django.shortcuts import render, get_object_or_404
from .models import About

# Create your views here.


def get_content(request):
    about = About.objects.order_by("-updated_on").first()
    return render(request, "about/about.html", {"about": about})
