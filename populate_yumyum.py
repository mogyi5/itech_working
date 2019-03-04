import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'working_project.settings')

import django
django.setup()
from yumyum.models import Category, Type, Ingredient, Recipe
from django.contrib.auth.models import User
from django.db import IntegrityError

def populate():

## superuser details
    username = 'itech'
    email = 'szaboki.reka@gmail.com'
    password = 'yumyum1234'

# The types of ingredient which can be selected
    types = {
    "Dairy":{"name": "Dairy"},
    "Meat":{"name": "Meat"},
    "Fruit":{"name": "Fruit"},
    "Vegetable":{"name": "Vegetable"},
    "Pasta":{"name": "Pasta"},
    "Grains":{"name": "Grains"},
    "Sauce":{"name": "Sauce"},
    "Snack":{"name": "Snack"},
    "Pastry":{"name": "Pastry"},
    "Seafood":{"name": "Seafood"},
    }

    for t in types:
        add_type(t)

# The recipe categories
    categories = {
    "Chinese":{"name": "Chinese"},
    "Vegan":{"name": "Vegan"},
    "Quick":{"name": "Quick"},
    "Indian":{"name": "Indian"},
    "Vegetarian":{"name": "Vegetarian"},
    "Pasta":{"name": "Pasta"},
    "Curry":{"name": "Curry"},
    "Stew":{"name": "Stew"},
    "Soup":{"name": "Soup"},
    "British":{"name": "British"},
    "Easy":{"name": "Easy"},
    "Light":{"name": "Light"},
    }

    for c in categories:
        add_cat(c)

    create_super_user(username, email, password)

    print("Population script finished!")

## adding the type
def add_type(name):
    t = Type.objects.get_or_create(name=name)
    #t.save()
    return t

## adding the category
def add_cat(name):
    c = Category.objects.get_or_create(name=name)
    #c.save()
    return c

## making a superuser
def create_super_user(username, email, password):
    try:
        u = User.objects.create_superuser(username, email, password)
        return u
    except IntegrityError:
        pass

# def add_ingredient(name, quantity=0, type):
#
#     return i

#def add_recipe():
#    return r

if __name__=='__main__':
	print("Starting YumYum population script...")
	populate()
