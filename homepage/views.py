from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request,"homepage/about.html")

def index(request):
    return render(request,"homepage/index.html")

def registration(request):
    return render(request,"homepage/registration.html")