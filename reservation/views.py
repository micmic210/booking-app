from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def reservation(request):
    return HttpResponse("Hello, Ramen Bar!")