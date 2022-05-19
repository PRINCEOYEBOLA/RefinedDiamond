from django.urls import path
from .views import homepage, index, registration

urlpatterns = [
    path("", homepage), 
    path("index/", index),
    path("registration/", registration)
       
]