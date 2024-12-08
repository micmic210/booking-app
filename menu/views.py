from django.shortcuts import render
from .models import Menu


def menu_view(request):
    """
    Displays menu items grouped by categories: ramen, starters, and appetizers.
    """
    ramen_items = Menu.objects.filter(
        category='ramen',
        is_available=True
    )
    starters_items = Menu.objects.filter(
        category='starters',
        is_available=True
    )
    appetizers_items = Menu.objects.filter(
        category='appetizers',
        is_available=True
    )

    return render(
        request,
        'menu/menu.html',
        {
            'ramen_items': ramen_items,
            'starters_items': starters_items,
            'appetizers_items': appetizers_items,
        }
    )
