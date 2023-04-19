from django.shortcuts import render
from .forms import FlightSearchForm
import requests
import json
from django.http import JsonResponse


def search_flights(request):
    form = FlightSearchForm()
    context = {
        'form': form
    }
    
    return render(request, 'flight_search.html', context)

