from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
# Create your views here.

def home(request:HttpRequest):
    return render(request,'home/home.html')

def under_work(request:HttpRequest):
    return render(request,'home/under_work.html')