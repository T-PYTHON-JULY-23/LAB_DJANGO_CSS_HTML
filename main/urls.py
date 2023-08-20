from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.home_view, name="home_view"),
    path("info/", views.about_view, name="info_view"),
    path("contact/", views.contact_view, name="contact_view"),
    path("conditionals/", views.conditionals_view, name="conditionals_view"),
    path("random/password/", views.random_pass_view, name="random_pass_view")
]