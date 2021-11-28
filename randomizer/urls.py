from django.urls import path
from randomizer import views

urlpatterns = [
    path('', views.homepage, name='home'),
]