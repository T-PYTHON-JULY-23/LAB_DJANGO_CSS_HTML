from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import random
import string

# Create your views here.



def home_view(request):
    return render(request, 'home.html')

