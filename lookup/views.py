from django.shortcuts import render

# https://www.airnowapi.org/aq/observation/zipCode/current/?format=text/csv&zipCode=89129&distance=5&API_KEY=B5FD4BAC-0E9B-4BB1-A32B-E027BED4EAB9

def home(request):
    import json
    import requests

    api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=text/csv&zipCode=89129&distance=5&API_KEY=B5FD4BAC-0E9B-4BB1-A32B-E027BED4EAB9")
    
    try:
        api = json.load(api_request.content)
    except Exception as e:
        api = "Error..."

    return render(request, 'home.html', {'api' : api})

def about(request):
    return render(request, 'about.html', {})