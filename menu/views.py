from django.shortcuts import render

# Create your views here.

def menu_view(request):
    return render(request, 'menu/menu.html')