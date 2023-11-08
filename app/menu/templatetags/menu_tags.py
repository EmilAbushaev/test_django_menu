from django import template
from ..models import MenuItem

register = template.Library()


@register.inclusion_tag('menu.html', takes_context=True)
def show_menu(context, filter=None):
    if not filter:
        menu_items = MenuItem.objects.all()
    else:
        menu_items = MenuItem.objects.filter(level=filter)
    return {"menu_items": menu_items}
