from django.shortcuts import render
from django.http import HttpResponse,HttpRequest

def m(request: HttpRequest):
    return render(request,"m.html")
# Create your views here.
