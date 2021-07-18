from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'shop/index.html')

def about(request):
    return HttpResponse('We are at About Page')

def contact(request):
    return HttpResponse('We are at Contact Page')

def tracker(request):
    return HttpResponse('We are at Tracker Page')

def search(request):
    return HttpResponse('We are at Search Page')

def productView(request):
    return HttpResponse('We are at ProductView Page')

def checkout(request):
    return HttpResponse('We are at checkout Page')