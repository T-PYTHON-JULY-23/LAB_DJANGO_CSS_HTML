from django.urls import path
from realestateapp import views


urlpatterns = [
    path('', views.home, name='home'),
]
