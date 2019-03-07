from django import template
from yumyum.models import Category

register = template.Library()


@register.inclusion_tag('yumyum/somethinghere.html')
def get_category_list():
    return {'somethinghere': Category.objects.all()}
