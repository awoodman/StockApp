from django.shortcuts import render

def home(request):
    import requests
    import json

    # pk_e57289f6fa8647d8a4a84b920f699b92
    api_request = requests.get("https://cloud.iexapis.com/stable/stock/aapl/quote?token=pk_e57289f6fa8647d8a4a84b920f699b92")

    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error..."

    return render(request, 'home.html', {'api':api})

def about(request):
    return render(request, 'about.html', {})