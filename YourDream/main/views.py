from django.shortcuts import render
from django.http import HttpRequest



def hom_viwes(request):
    return render(request ,'pages/home.html')