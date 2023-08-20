from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import random
import string

# Create your views here.


def home_view(request : HttpRequest):
    
    return render(request, "main/home.html")


def about_view(request : HttpRequest):

    return render(request, "main/info.html")


def contact_view(request : HttpRequest):

    #to pass data to a template we user Context
    context = {"email" : "info@carentals.com", "phone" : "+966 0937837"}

    return render(request, "main/contact.html", context)


def conditionals_view(request : HttpRequest):

    products = ["Juice", "Hamburger", "French Fries"]

    context = {"is_dilvered" : False, "products" : products}

    return render(request, "main/coditionals.html", context)



def random_pass_view(request: HttpRequest):

    random_pass = random.choices(string.ascii_letters+string.digits+string.punctuation, k=15)

    random_pass_string = "".join(random_pass)
    context = {"pass" : random_pass_string}

    return render(request, "main/random_pass.html", context)