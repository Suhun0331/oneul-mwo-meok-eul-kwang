from django.urls import path
from . import views

app_name = 'kweat'

urlpatterns = [
    #path('', views.index, name='index'),
    path('filter/', views.filter, name='filter'),
    path('roulette/', views.roulette, name='roulette'),
    path('questions/', views.questions, name='questions'),
]