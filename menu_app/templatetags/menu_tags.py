from django import template
from menu_app.models import MenuItem
from django.utils.safestring import mark_safe
from django.urls import reverse
from urllib.parse import urljoin

register = template.Library()

def _draw_menu_recursive(menu_items, parent_url='', active_page=''):
    result = '<ul>'
    class_name = ''
    
    for menu_item in menu_items:
        if menu_item.parent is None:
            class_name = 'parent'
        else:
            class_name = 'child'

        menu_url = reverse(menu_item.url) 
        
        if active_page == menu_url:
            class_name += ' active'

        result += f'<li class="{class_name}">'
        child_url = urljoin(parent_url, menu_url) if parent_url else menu_url
        result += f'<a href="{child_url}">{menu_item.name}</a>'
        
        try:
            result += _draw_menu_recursive(menu_item.children.all(), child_url, active_page)
        except:
            pass
        result += '</li>'
    
    result += '</ul>'
    
    return result

@register.simple_tag
def draw_menu(menu_name, path):
    menu_items = MenuItem.objects.filter(menuName=menu_name)
    print(path)
    return mark_safe(_draw_menu_recursive(menu_items, active_page=path))