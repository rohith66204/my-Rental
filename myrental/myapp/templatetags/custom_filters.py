from django import template
from ..models import sell

register = template.Library()

@register.filter
def house_count(house_type):
    return sell.objects.filter(house_type=house_type).count()