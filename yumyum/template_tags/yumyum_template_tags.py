from django import template
from yumyum.models import Category

register = template.Library()


@register.inclusion_tag('yumyum/cats.html')
def get_category_list(cat=None):
    return {'cats': Recipe.objects.all(),
            'act_cat': cat}
