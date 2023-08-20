from django.shortcuts import render
from django.http import HttpRequest , HttpResponse


def home_page(request : HttpRequest):

    return render(request, "main/homePage.html")

# Create your views here.
