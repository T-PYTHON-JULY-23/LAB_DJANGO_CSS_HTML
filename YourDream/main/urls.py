from django.urls import path
from . import views

app_name = "main"


urlpatterns = [
    path("", views.hom_viwes, name="home_view")
]