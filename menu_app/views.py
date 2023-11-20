from django.shortcuts import render
from menu_app.models import MenuItem
from menu_app.templatetags.menu_tags import _draw_menu_recursive

def menu_page(request):
    return render(request, 'menu_app/menu_page.html')
