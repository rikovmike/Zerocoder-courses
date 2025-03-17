from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    data = {
        'caption':"Rikovmike"
    }
    return render(request, 'main/index.html',data)
def new(request):
    return render(request, 'main/new.html')

def portfolio(request):
    return render(request, 'main/portfolio.html')

def map(request):
    return render(request, 'main/map.html')

def gallery(request):
    return render(request, 'main/gallery.html')

def blog(request):
    return render(request, 'main/blog.html')

