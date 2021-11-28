from django.urls import path
from randomizer import views

urlpatterns = [
    path('', views.teams_overview, name='teams_overview'),
    path('', views.homepage, name='home'),

]