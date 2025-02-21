from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, ("core/home.html"))

def about(request):
    return render(request, ("core/about.html"))

def features(request):
    return render(request, ("core/features.html"))

def pricing(request):
    return render(request, ("core/pricing.html"))

def help(request):
    return render(request, ("core/help.html"))

def safety(request):
    return render(request, "safety.html")