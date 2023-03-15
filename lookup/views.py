from django.shortcuts import render

def home(request):
    import json
    import requests

    if request.method == "POST":
        zipcode = request.POST['zipcode']
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=5&API_KEY=B5FD4BAC-0E9B-4BB1-A32B-E027BED4EAB9")

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."

        if api[0]['Category']['Name'] == "Good":
            category_description = "(0-50)"
            category_color = "good"
        elif api[0]['Category']['Name'] == "Moderate":
            category_description = "(51-100)"
            category_color = "moderate"
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":    
            category_description = "(101-150)"
            category_color = "usg"
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_description = "(151-200)"
            category_color = "unhealthy"
        elif api[0]['Category']['Name'] == "Very Unhealthy":    
            category_description = "(200-300)"
            category_color = "veryunhealty"
        elif api[0]['Category']['Name'] == "Hazardous":
            category_description = "(301-500)"
            category_color = "hazardous"
    
        return render(request, 'home.html', { 
         'api' : api, 
         'category_description' : category_description, 
         'category_color' : category_color })


    else:
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=B5FD4BAC-0E9B-4BB1-A32B-E027BED4EAB9")

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."

        if api[0]['Category']['Name'] == "Good":
            category_description = "(0-50)"
            category_color = "good"
        elif api[0]['Category']['Name'] == "Moderate":
            category_description = "(51-100)"
            category_color = "moderate"
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":    
            category_description = "(101-150)"
            category_color = "usg"
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_description = "(151-200)"
            category_color = "unhealthy"
        elif api[0]['Category']['Name'] == "Very Unhealthy":    
            category_description = "(200-300)"
            category_color = "veryunhealty"
        elif api[0]['Category']['Name'] == "Hazardous":
            category_description = "(301-500)"
            category_color = "hazardous"
        
        return render(request, 'home.html', { 
         'api' : api, 
         'category_description' : category_description, 
         'category_color' : category_color })


def about(request):
    return render(request, 'about.html', {})