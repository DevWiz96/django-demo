from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
# Create your views here.

def home(request):
       return HttpResponse("Django service is running")

def flask_status(request):
       try:
              response = requests.get('http://localhost:5000/api/status',timeout=3)
              response.raise_for_status()

              return JsonResponse({
                     "Service":"Django",
                     "flask-server":response.json()
              })
       except(requests.RequestException, ValueError):
            return JsonResponse({
                     "Service":"Django",
                     "flask-server": "Undefined"
              },status = 502)


    
