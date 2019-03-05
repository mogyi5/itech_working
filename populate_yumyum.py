import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'working_project.settings')

import django
django.setup()
from yumyum.models import Category, Type, Ingredient, Recipe, RecipeIngredient, UserProfile
from django.contrib.auth.models import User
from django.db import IntegrityError

def populate():

## superuser details
    username = 'itech'
    email = 'szaboki.reka@gmail.com'
    password = 'yumyum1234'

    super = create_super_user(username, email, password)

# making some new users for fun
    user1 = User.objects.create_user(username='john',email='jlennon@beatles.com',password='glass onion' )
    user2 = User.objects.create_user(username='donald',email='donald@trump.com',password='billions' )
    user3 = User.objects.create_user(username='ru',email='dragrace@vh1.com',password='kittygirl')

    Categories = {"Light":{
    "Curried Fish & Leek Noodles" : { "servings":2, "cooking_time":10, "direction":"Defrost the frozen fish fillet in the fridge overnight. The next day, season the fish with salt and pepper and dust with the curry powder. Pan-fry it in a splash of olive oil over a medium heat until cooked. It will take about 5 minutes on each side, depending on the thickness of the fillet. Add the leek ribbons to the frying pan and cook them along with the fish. Serve the fish on a bed of leek noodles.", "user":user2},
    },
    "Pasta":{
    "Smoked Mackerel & Kale Carbonara": { "servings":2, "cooking_time":15, "direction":"Bring a large pan of salted water to the boil and cook the spaghetti until al denta, throwing in the kale about 2 minutes before it's ready. Meanwhile, grab a bowl and mix the egg yolks with the grated parmesan and plenty of cracked black pepper. When the spaghetti and kale are cooked, transfer them to the bowl using tongs and mix everything together (the heat of the spaghetti will cook the egg yolk and create the sauce). Add a tablespoon of the cooking water to the pasta along with the flaked smoked mackerel, season if required, and serve with a drizzle of olive oil.", "user":user1,}
    },
    "Main":{
    "Chicken & Creamed Spinach": {"servings": 2, "cooking_time": 40, "direction": "Season the chicken thigh with salt and pepper. Pan-fry it skin-side down in a splash of olive oil over a medium heat. After about 10 minutes, when the skin is golden brown, turn it over and cook it for a further 10 minutes. Add the garlic and, just as it starts to brown, throw in the cannelini beans and then the spinach. Once the spinach has wilted and the chicken in cooked through, pour over the cream, season again with salt and pepper, then simmer for a few minutes to thicken the sauce a bit and serve.", "user": user1,},
    "Leek Tatin Quiche": { "servings":2, "cooking_time":30, "direction":"Grab a really small pan and place the leeks in it, standing them up like soldiers. Drizzle with a generous glug of olive oil, season with salt and pepper and start pan-frying over a medium heat. After about 10 minutes, turn each piece of leek over to cook on the other side. While the leeks continue cooking, whisk the eggs and season with salt and pepper. Preheat the grill. Pour the eggs over the leeks. Turn the heat down to low and cook slowly for about 10 minutes until the egg is almost cooked. Place the pan under the hot grill until the top is completely cooked and golden brown. Eat from pan.", "user":user3,}
    },
    "Vegetarian":{
    "Welsh Rarebit": { "servings":2, "cooking_time":5, "direction":"Preheat your Grill to high. Mix the grated cheese and cream together in a bowl to create a cheesy spread with the consistency of mashed potato. Spread it onto the bread slices, top each slice with two halves of spring onion, splash with Worcestershire sauce, then cook under the grill for a few minutes until the cheese melts and starts to brown. Remove from the grill, sprinkle with cracked black pepper and serve straightaway.", "user":user3,},
    "White Bean Dauphinoise": { "servings": 2, "cooking_time": 35, "direction": "Preheat your oven to 190C/gas mark 5. Throw the cannelini beans into an ovenproof dish with the garlic. Pour over the cream and sprinkle over most of the grated parmesan. Season with salt and pepper then stir everything together and bake in the oven for about 25 minutes. Once cooked, serve sprinkled with the remaining parmesan and some cracked black pepper.", "user":user2,},
    },
    }

    for c, c_data in Categories.items():
        cat = add_cat(c)
        for i, i_data in c_data.items():
             add_recipe(i,i_data["servings"],cat,i_data["cooking_time"], i_data["direction"], i_data["user"])

    # Create ingredients by type
    Types = {"Dairy": {
    "Milk", "Cheddar", "Mozzarella", "Brie", "Single Cream", "Whipping Cream", "Parmesan"
    },
    "Meat": {
    "Beef Mince", "Lamb Chops", "Pork Steak", "Chicken Nuggets", "Chicken Breast", "Chicken Thighs", "Chicken Wings", "Bacon", "Fish Fillet", "Smoked Mackerel"
    },
    "Fruit": {
    "Bananas", "Apples", "Oranges", "Lemons", "Raspberries", "Kiwis", "Mandarins", "Strawberries"
    },
    "Vegetables":{
    "Spring Onions", "Onions", "Carrots", "Cabbage", "Iceberg Lettuce", "Bell Peppers", "Peas", "Potatoes", "Spinach", "Leeks", "Kale"
    },
    "Seasoning":{
    "Cumin", "Black Pepper", "White Pepper", "Salt", "Paprika", "Cayenne Pepper", "Cinnamon", "Cayenne Pepper", "Garlic", "Curry Powder"
    },
    "Sauces":{
    "Worcestershire Sauce", "Sweet Chilli Sauce", "Soy Sauce", "Vinegar", "Cooking Wine", "Tomato Sauce"
    },
    "Cupboard":{
    "Bread", "Flour", "Sugar", "Yeast", "Honey", "Lentils", "Canned Beans", "Canned Sweetcorn", "Dried Spaghetti", "Rice", "Olive Oil", "Eggs"
    }
    }

    # Add the ingredients in each type
    for t, t_data in Types.items():
        type = add_type(t)
        for i in t_data:
            add_ingredient(i, type)

# class Sample(models.Model):
#      users = models.ManyToManyField(User)
#
# user1 = User.objects.get(pk=1)
# user2 = User.objects.get(pk=2)
# sample_object = Sample( users = user1, users=user2 )
# sample_object.save()
#
# sample_object = Sample()
# sample_object.save()
# sample_object.users.add(1,2)

# (recipe, ingredient, quantity, unit)

##make arrays or sth with the name of the recipe, then for each array get the object from recipe and make that the thing of the thing, then get the ingredient's type too, add manually the quantities and units.
#Recipe.objects.get
    "Curried Fish & Leek Noodles":{"ingredient":""

    },
    "Smoked Mackerel & Kale Carbonara":{

    },
    "Chicken & Creamed Spinach":{

    },
    "Leek Tatin Quiche":{

    },
    "Welsh Rarebit":{

    },
    "White Bean Dauphinoise":{

    },
    }

    print("Population script finished!")


## adding the type
def add_type(name):
    t = Type.objects.get_or_create(name=name)[0]
    return t

## adding the category
def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    return c

## adding the ingredient
def add_ingredient(name, type):
    i = Ingredient.objects.get_or_create(name=name)[0]
    i.type = type
    i.save()
    return i

# adding the recipe
def add_recipe(title, servings, category, cooking_time, direction, user):
    r = Recipe.objects.get_or_create(category=category, title=title, servings = servings, cooking_time = cooking_time, direction = direction, user = user)[0]
    r.save()
    return r

def add_recipeingredient(recipe, ingredient, quantity, unit):
    ri = RecipeIngredient.objects.get_or_create(recipe = recipe, ingredient = ingredient, quantity = quantity, unit=unit)[0]
    ri.save()
    return ri

## making a superuser
def create_super_user(username, email, password):
    try:
        u = User.objects.create_superuser(username, email, password)
        return u
    except IntegrityError:
        pass


if __name__=='__main__':
	print("Starting YumYum population script...")
	populate()
