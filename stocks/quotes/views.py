from django.shortcuts import render

def home(request):
    # pk_e57289f6fa8647d8a4a84b920f699b92
    return render(request, 'home.html', {})

def about(request):
    return render(request, 'about.html', {})