from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def main_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'main/index.html')
