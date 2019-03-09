import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'working_project.settings')

import django
django.setup()
from yumyum.models import Category, Type, Ingredient, Recipe, RecipeIngredient, Review, UserProfile
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

    Profiles = {
    "john":{"about": "I am a fun loving, free guy that loves to spice up his life. I am 23 and work all the time so the only way I can express myself is through cooking: by making literally spicy food so I feel the weight of the world crush me less."},
    "donald":{"about": "I'm not actually Donald Trump, but the username wasn't taken so I thought why not? I still live with my parents but I feel better if I can help with the cooking... It is hard to get a job after graduation! Shame I studied English Literature instead of something useful at university!"},
    "ru":{"about": "I am 28, single, and ready to make some kick-ass food for my pet chihuahua."}
    }

    for p, p_data in Profiles.items():
        add_profile(User.objects.get(username = p), p_data["about"])



    Categories = {"Light":{
    "Curried Fish & Leek Noodles" : { "servings":2, "cooking_time":10, "direction":"Defrost the frozen fish fillet in the fridge overnight. The next day, season the fish with salt and pepper and dust with the curry powder. Pan-fry it in a splash of olive oil over a medium heat until cooked. It will take about 5 minutes on each side, depending on the thickness of the fillet. Add the leek ribbons to the frying pan and cook them along with the fish. Serve the fish on a bed of leek noodles.", "user":user2},
    },
    "Pasta":{
    "Smoked Mackerel & Kale Carbonara": { "servings":2, "cooking_time":15, "direction":"Bring a large pan of salted water to the boil and cook the spaghetti until al denta, throwing in the kale about 2 minutes before it's ready. Meanwhile, grab a bowl and mix the egg yolks with the grated parmesan and plenty of cracked black pepper. When the spaghetti and kale are cooked, transfer them to the bowl using tongs and mix everything together (the heat of the spaghetti will cook the egg yolk and create the sauce). Add a tablespoon of the cooking water to the pasta along with the flaked smoked mackerel, season if required, and serve with a drizzle of olive oil.", "user":user1,}
    },
    "Main":{
    "Chicken & Creamed Spinach": {"servings": 2, "cooking_time": 40, "direction": "Season the chicken thigh with salt and pepper. Pan-fry it skin-side down in a splash of olive oil over a medium heat. After about 10 minutes, when the skin is golden brown, turn it over and cook it for a further 10 minutes. Add the garlic and, just as it starts to brown, throw in the cannellini beans and then the spinach. Once the spinach has wilted and the chicken in cooked through, pour over the cream, season again with salt and pepper, then simmer for a few minutes to thicken the sauce a bit and serve.", "user": user1,},
    "Leek Tatin Quiche": { "servings":2, "cooking_time":30, "direction":"Grab a really small pan and place the leeks in it, standing them up like soldiers. Drizzle with a generous glug of olive oil, season with salt and pepper and start pan-frying over a medium heat. After about 10 minutes, turn each piece of leek over to cook on the other side. While the leeks continue cooking, whisk the eggs and season with salt and pepper. Preheat the grill. Pour the eggs over the leeks. Turn the heat down to low and cook slowly for about 10 minutes until the egg is almost cooked. Place the pan under the hot grill until the top is completely cooked and golden brown. Eat from pan.", "user":user3,}
    },
    "Vegetarian":{
    "Welsh Rarebit": { "servings":2, "cooking_time":5, "direction":"Preheat your Grill to high. Mix the grated cheese and cream together in a bowl to create a cheesy spread with the consistency of mashed potato. Spread it onto the bread slices, top each slice with two halves of spring onion, splash with Worcestershire sauce, then cook under the grill for a few minutes until the cheese melts and starts to brown. Remove from the grill, sprinkle with cracked black pepper and serve straightaway.", "user":user3,},
    "White Bean Dauphinoise": { "servings": 2, "cooking_time": 35, "direction": "Preheat your oven to 190C/gas mark 5. Throw the cannellini beans into an ovenproof dish with the garlic. Pour over the cream and sprinkle over most of the grated parmesan. Season with salt and pepper then stir everything together and bake in the oven for about 25 minutes. Once cooked, serve sprinkled with the remaining parmesan and some cracked black pepper.", "user":user2,},
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
    "Spring Onions", "Onions", "Carrots", "Cabbage", "Iceberg Lettuce", "Bell Peppers", "Peas", "Potatoes", "Spinach", "Leeks", "Kale", "Cannellini Beans"
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

# What ingredients are in the recipes? ALso units and stuff
    RecipeIngredients = {
    "Curried Fish & Leek Noodles":
    {"Fish Fillet":{"quantity":2, "unit":'pieces'},
    "Curry Powder":{"quantity":2, "unit":'tsp'},
    "Leeks":{"quantity":1, "unit":'pieces'},
    "Olive Oil":{"quantity":1, "unit":'tbsp.'},
    "Salt":{"quantity":1, "unit":'pinch'},
    "Black Pepper":{"quantity":1, "unit":'pinch'}
    },
    "Smoked Mackerel & Kale Carbonara":{
    "Dried Spaghetti":{"quantity":250, "unit":'g'},
    "Kale":{"quantity":50, "unit":'g'},
    "Eggs":{"quantity":4, "unit":'pieces'},
    "Parmesan":{"quantity":25, "unit":'g'},
    "Smoked Mackerel":{"quantity":100, "unit":'g'},
    "Olive Oil":{"quantity":1, "unit":'tbsp.'},
    "Salt":{"quantity":1, "unit":'pinch'},
    "Black Pepper":{"quantity":1, "unit":'pinch'}
    },
    "Chicken & Creamed Spinach":{
    "Chicken Thighs":{"quantity":2, "unit":'pieces'},
    "Garlic":{"quantity":2, "unit":'cloves'},
    "Cannellini Beans":{"quantity":400, "unit":'g'},
    "Spinach":{"quantity":50, "unit":'g'},
    "Single Cream":{"quantity":150, "unit":'ml'},
    "Olive Oil":{"quantity":1, "unit":'tbsp.'},
    "Salt":{"quantity":1, "unit":'pinch'},
    "Black Pepper":{"quantity":1, "unit":'pinch'}
    },
    "Leek Tatin Quiche":{
    "Leeks":{"quantity":2, "unit":'pieces'},
    "Eggs":{"quantity":6, "unit":'pieces'},
    "Olive Oil":{"quantity":1, "unit":'tbsp.'},
    "Salt":{"quantity":1, "unit":'pinch'},
    "Black Pepper":{"quantity":1, "unit":'pinch'}
    },
    "Welsh Rarebit":{
    "Cheddar":{"quantity":75, "unit":'g'},
    "Bread":{"quantity":4, "unit":'slices'},
    "Spring Onions":{"quantity":4, "unit":'pieces'},
    "Single Cream":{"quantity":75, "unit":'ml'},
    "Worcestershire Sauce":{"quantity":1, "unit":'tbsp.'},
    "Black Pepper":{"quantity":1, "unit":'pinch'}
    },
    "White Bean Dauphinoise":{
    "Cannellini Beans":{"quantity":400, "unit":'g'},
    "Garlic":{"quantity":2, "unit":'cloves'},
    "Single Cream":{"quantity":200, "unit":'ml'},
    "Parmesan":{"quantity":50, "unit":'g'},
    "Salt":{"quantity":1, "unit":'pinch'},
    "Black Pepper":{"quantity":1, "unit":'pinch'}
    },
    }

# Add ingredients to the recipes above.
    for rec, rec_data in RecipeIngredients.items():
        for i, i_data in rec_data.items():
            add_recipeingredient(Recipe.objects.get(title=rec), Ingredient.objects.get(name=i), i_data["quantity"], i_data["unit"])

    print("Population script finished!")

# Some comments for the recipes
    Comments = {
    "Tasty!" : {"rating": 4, "comment_body": "Made it for my fussy son and he loved it! So easy and quick!", "user": user1, "recipe":"Welsh Rarebit"},
    "Best meal I have ever had!" : {"rating": 5, "comment_body": "I literally cried, this was so good...", "user": user2, "recipe":"Chicken & Creamed Spinach"},
    }

# Add a couple of reviews
    for c, c_data in Comments.items():
        add_reviews(c_data["rating"], c, c_data["comment_body"], c_data["user"], Recipe.objects.get(title=c_data["recipe"]))

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

# add recipe ingredients
def add_recipeingredient(recipe, ingredient, quantity, unit):
    ri = RecipeIngredient.objects.get_or_create(recipe = recipe, ingredient = ingredient, quantity = quantity, unit=unit)[0]
    ri.save()
    return ri

# add comments
def add_reviews(rating, comment_title, comment_body, user, recipe):
    rev = Review.objects.get_or_create(rating = rating, comment_title = comment_title, comment_body = comment_body, user = user, recipe = recipe)[0]
    #rev.save()
    return rev

# make profiles for the users
def add_profile(user, about):
    p = UserProfile.objects.get_or_create(user = user, about=about)[0]
    return p

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