from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


# Create your views here.
def blog(request):
    return HttpResponse("hello world")
