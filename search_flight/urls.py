from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_flights, name="search_flights"),
    #path('autocomplete/', views.autocomplete, name='autocomplete'),

    #path('flights',views.flights, name="flights"),  
]
