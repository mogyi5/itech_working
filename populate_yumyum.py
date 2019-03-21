import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'working_project.settings')

import django
django.setup()
from yumyum.models import Category, Type, Ingredient, Recipe, RecipeIngredient, Review, UserProfile
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.core.files import File

def populate():

## making a superuser
    username = 'itech'
    email = 'szaboki.reka@gmail.com'
    password = 'yumyum1234'

    super = create_super_user(username, email, password)

# making some new users for fun
    user1 = User.objects.create_user(username='john',email='jlennon@beatles.com',password='glass onion' )
    user2 = User.objects.create_user(username='donald',email='donald@trump.com',password='billions' )
    user3 = User.objects.create_user(username='ru',email='dragrace@vh1.com',password='kittygirl')

# populating the profiles also
    Profiles = {
    "john":{"img":File(open('./media/profile_images/john.JPG','rb')), "about": "I am a fun loving, free guy that loves to spice up his life. I am 23 and work all the time so the only way I can express myself is through cooking: by making literally spicy food so I feel the weight of the world crush me less."},
    "donald":{"img":File(open('./media/profile_images/don.JPG','rb')) ,"about": "I'm not actually Donald Trump, but the username wasn't taken so I thought why not? I still live with my parents but I feel better if I can help with the cooking... It is hard to get a job after graduation! Shame I studied English Literature instead of something useful at university!"},
    "ru":{"img":File(open('./media/profile_images/ru.JPG','rb')) , "about": "I am 28, single, and ready to make some kick-ass food for my pet chihuahua."}
    }

    for p, p_data in Profiles.items():
        add_profile(User.objects.get(username = p), p_data["img"], p_data["about"])


# have recipes in each category
    Categories = {"Light":{
    "Curried Fish & Leek Noodles" : { "servings":2, "cooking_time":10, "direction":"Defrost the frozen fish fillet in the fridge overnight. The next day, season the fish with salt and pepper and dust with the curry powder. Pan-fry it in a splash of olive oil over a medium heat until cooked. It will take about 5 minutes on each side, depending on the thickness of the fillet. Add the leek ribbons to the frying pan and cook them along with the fish. Serve the fish on a bed of leek noodles.", "user":user2, "img":File(open('./media/recipe_images/curried-fish.JPG','rb'))},
    "Maple Tamarind Glazed Salmon" : { "servings":4, "cooking_time":30, "direction":" Preheat the oven to 425F degrees and line a baking sheet with parchment paper. Season the salmon portions lightly with salt and pepper and lay a couple of inches apart on the prepared baking sheet. Whisk all of the ingredients for the glaze together until well combined. Liberally brush the glaze all over the salmon pieces. Bake for 10 minutes, then reapply another layer of the glaze and bake for an additional 10 minutes. Serve immediately.", "user":user3, "img":File(open('./static/images/slide3.jpg','rb'))},
    },
    "Pasta":{
    "Smoked Mackerel & Kale Carbonara": { "servings":2, "cooking_time":15, "direction":"Bring a large pan of salted water to the boil and cook the spaghetti until al dente, throwing in the kale about 2 minutes before it's ready. Meanwhile, grab a bowl and mix the egg yolks with the grated parmesan and plenty of cracked black pepper. When the spaghetti and kale are cooked, transfer them to the bowl using tongs and mix everything together (the heat of the spaghetti will cook the egg yolk and create the sauce). Add a tablespoon of the cooking water to the pasta along with the flaked smoked mackerel, season if required, and serve with a drizzle of olive oil.", "user":user1,"img":File(open('./media/recipe_images/carbonara.JPG','rb'))},
    "Basically Spaghetti Pomodoro": { "servings":4, "cooking_time":35, "direction":"Bring a large pan of salted water to the boil. Meanwhile, open the can of tomatoes, drain contents in a colander set over a medium bowl. Poke a hole in the tomatoes and shake to drain liquid and seeds from the inside of each tomato. Set aside. Heat oil in a large pan, add smashed cloves of garlic and cook, stirring often until garlic is golden - about 3 minutes. Stir in the red pepper flakes and add drained tomatoes; increade heat to medium-high. Cook, stirring occasionally, until tomatoes are starting to break down, 6-8 minutes. Add reserved tomato liquid, add salt, basil, and reduce heat to a simmer. Cook until liquid is reduced, 8-10 minutes. Add pasta to the pot of water and cook, stirring occasionally.Just before it's done, scoop out one cup of cooking fluid with a heatproof measuring cup. When al dente, transfer the pasta to the pot with the tomatoes, and add half of the reserved cooking liquid. Cook the pasta, tossing constantly, until liquid is mostly absorbed. Slowly sprinkle in half of the parmesan, and toss until it melts into the sauce. Add more pasta water, until the sauce oozes. Remove pot from heat and add butter. Add finished pasta to plates and top with remaining cheese and basil leaves.", "user":user1,"img":File(open('./static/images/slide2.jpg','rb'))},
    },
    "Main":{
    "Chicken & Creamed Spinach": {"servings": 2, "cooking_time": 40, "direction": "Season the chicken thigh with salt and pepper. Pan-fry it skin-side down in a splash of olive oil over a medium heat. After about 10 minutes, when the skin is golden brown, turn it over and cook it for a further 10 minutes. Add the garlic and, just as it starts to brown, throw in the cannellini beans and then the spinach. Once the spinach has wilted and the chicken in cooked through, pour over the cream, season again with salt and pepper, then simmer for a few minutes to thicken the sauce a bit and serve.", "user": user1,"img":File(open('./media/recipe_images/creamed.JPG','rb'))},
    "Leek Tatin Quiche": { "servings":2, "cooking_time":30, "direction":"Grab a really small pan and place the leeks in it, standing them up like soldiers. Drizzle with a generous glug of olive oil, season with salt and pepper and start pan-frying over a medium heat. After about 10 minutes, turn each piece of leek over to cook on the other side. While the leeks continue cooking, whisk the eggs and season with salt and pepper. Preheat the grill. Pour the eggs over the leeks. Turn the heat down to low and cook slowly for about 10 minutes until the egg is almost cooked. Place the pan under the hot grill until the top is completely cooked and golden brown. Eat from pan.", "user":user3,"img":File(open('./media/recipe_images/leek.JPG','rb'))}
    },
    "Vegetarian":{
    "Welsh Rarebit": { "servings":2, "cooking_time":5, "direction":"Preheat your Grill to high. Mix the grated cheese and cream together in a bowl to create a cheesy spread with the consistency of mashed potato. Spread it onto the bread slices, top each slice with two halves of spring onion, splash with Worcestershire sauce, then cook under the grill for a few minutes until the cheese melts and starts to brown. Remove from the grill, sprinkle with cracked black pepper and serve straightaway.", "user":user3,"img":File(open('./media/recipe_images/welsh.JPG','rb'))},
    "White Bean Dauphinoise": { "servings": 2, "cooking_time": 35, "direction": "Preheat your oven to 190C/gas mark 5. Throw the cannellini beans into an ovenproof dish with the garlic. Pour over the cream and sprinkle over most of the grated parmesan. Season with salt and pepper then stir everything together and bake in the oven for about 25 minutes. Once cooked, serve sprinkled with the remaining parmesan and some cracked black pepper.", "user":user2, "img":File(open('./media/recipe_images/dauphinoise.JPG','rb'))},
    "Grilled Vegetable Wrap": { "servings":2, "cooking_time": 25, "direction": "1. Preheat grill or broiler. Toss together asparagus, bell pepper, squash, and oil on large baking sheet. Season with salt and pepper, if desired. Grill or broil vegetables 4 to 6 minutes per side, turning once. 2. Mash together beans, garlic, and chile sauce in small bowl until smooth. 3. Spread half of bean mixture over each tortilla. Top each with 3 basil leaves, 1/2 cup roasted vegetables, 4 onion slices, and 1/2 cup arugula. Fold bottom third of tortillas over vegetables, and roll up tightly, tucking in sides as you go. Cut wraps in half on diagonal. Serve immediately, or wrap each half in foil or wax paper, and chill until ready to eat.", "user":user1, "img":File(open('./static/images/slide1.jpg','rb'))},
    },
    "Cakes":{
    "Blueberry Coffee Cake":{"servings":12, "cooking_time":90, "direction":"Mix butter, 1 cup sugar, flour, 2 eggs, 2 tsp vanilla, baking powder, and milk to make cake batter. Blend easily.  Add 3 cups of blueberries.  Put 2 1/2 cups of batter in pan. Mix cream cheese, 1/2 cup sugar, 1 egg, lemon juice and 1 tsp vanilla to make filling.  Put filling on top of batter.  Top with remaining batter. Make streusel topping from flour, butter, brown sugar, ad cinnamon.  Sprinkle on top of cake. Bake at 375 degrees for 1 hour and 5 minutes.  Check after 50 minutes.", "user":user3,"img":File(open('./media/recipe_images/blu.jpg','rb'))},
    "Chocolate Cake":{"servings":15, "cooking_time":60, "direction":"Mix all ingredients together.  Pour in 1 cup boiling water.  Mix well. Bake about 35 minutes at 375 degrees.", "user":user1,"img":File(open('./media/recipe_images/choc.jpg','rb'))},
    "Crazy Cake":{"servings":12, "cooking_time":45, "direction":"Mix first 5 ingredients well, about 4 minutes.  Bake at 350 degrees in a 9x13 pan for 35 minutes. Poke holes in warm cake and pour on mixture of powdered sugar and lemon juice.", "user":user1, "img":File(open('./media/recipe_images/cray.jfif','rb'))},
    "Fresh Apple Cake":{"servings":12, "cooking_time":60, "direction":"Mix apples and sugar well.  Add oil, nuts, and eggs.  Add vanilla and dry ingredients.  Bake at 350 degrees for 40-45 minutes.  Serve with whipped cream or top with cream cheese frosting.", "user":user1, "img":File(open('./media/recipe_images/apple_cake.jpg','rb'))},
    "Fresh Pear Cake":{"servings":10, "cooking_time":75, "direction":"Butter and flour a 9 inch round pan.  Peel and slice pears.  Blend eggs, sugar, milk, and salt.  Add flour, mix well.  Fold 1/2 of pears into batter.  Pour into pan, fan remaining pears on top.  Dot with butter.  Bake at 350 degrees about 55 minutes.  Sprinkle with powdered sugar.", "user":user3,"img":File(open('./media/recipe_images/pear_cake.jpg','rb'))},
    "Graham Cracker Cake":{"servings":8, "cooking_time":45, "direction":"Cream butter and sugar.  Add crushed crackers, sour milk, and soda.  Stir in nuts.  Bake in 10 inch square baking pan.  Bake in 350 degree oven for 30-35 minutes.  Serve with whipped cream or thin powdered sugar icing.", "user":user1, "img":File(open('./media/recipe_images/grah_cake.jpg','rb'))},
    "Hot Water Chocolate Cake":{"servings":12, "cooking_time":45, "direction":"Mix all ingredients together.  Pour in 1 cup boiling water. Mix well.  Bake about 35 minutes at 375 degrees.", "user":user2, "img":File(open('./media/recipe_images/hot_water.jpg','rb'))},
    },
    }

    for c, c_data in Categories.items():
        cat = add_cat(c)
        for i, i_data in c_data.items():
             add_recipe(i,i_data["servings"],cat,i_data["cooking_time"], i_data["direction"], i_data["user"], i_data["img"])

    # Create ingredients by type
    Types = {"Dairy": {
    "Milk", "Cheddar", "Mozzarella", "Brie", "Single Cream", "Whipping Cream", "Parmesan", "Butter", "Cream Cheese", "Sour Milk"
    },
    "Meat": {
    "Beef Mince", "Lamb Chops", "Pork Steak", "Chicken Nuggets", "Chicken Breast", "Chicken Thighs", "Chicken Wings", "Bacon", "Fish Fillet", "Smoked Mackerel"
    },
    "Fruit": {
    "Bananas", "Apples", "Oranges", "Lemons", "Raspberries", "Kiwis", "Mandarins", "Strawberries","Blueberries", "Pears"
    },
    "Vegetables":{
    "Spring Onions", "Onions", "Carrots", "Cabbage", "Iceberg Lettuce", "Bell Peppers", "Peas", "Potatoes", "Spinach", "Leeks", "Kale", "Cannellini Beans", "Asparagus Spears", "Squash", "Red Onions", "Arugula Leaves"
    },
    "Seasoning":{
    "Cumin", "Black Pepper", "White Pepper", "Salt", "Paprika", "Cayenne Pepper", "Cinnamon", "Cayenne Pepper", "Garlic", "Curry Powder", "Basil Leaves", "Grated Ginger", "Chilli Flakes", "Chinese Five Spice", "Vanilla", "Cloves"
    },
    "Sauces":{
    "Worcestershire Sauce", "Sweet Chilli Sauce", "Soy Sauce", "Vinegar", "Cooking Wine", "Tomato Sauce", "Sriracha Sauce", "Maple Syrup"
    },
    "Cupboard":{
    "Bread", "Flour", "Sugar", "Yeast", "Honey", "Lentils", "Canned Beans", "Canned Sweetcorn", "Dried Spaghetti", "Rice", "Olive Oil", "Eggs", "Tortillas", "Tamarind Paste", "Canned Tomatoes", "Lemon Juice", "Baking Powder", "Cocoa", "Lemon Cake Mix", "Lemon Jello", "Vegetable Oil", "Nuts", "Baking Soda", "Graham Crackers"
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
    "Curry Powder":{"quantity":2, "unit":'tsp.'},
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
    "Grilled Vegetable Wrap":{
    "Asparagus Spears":{"quantity":12, "unit":'pieces'},
    "Bell Peppers":{"quantity":1, "unit":'pieces'},
    "Squash":{"quantity":1, "unit":'pieces'},
    "Olive Oil":{"quantity":1, "unit":'tbsp.'},
    "Canned Beans":{"quantity":250, "unit":'g'},
    "Garlic":{"quantity":1, "unit":'cloves'},
    "Sriracha Sauce":{"quantity":0.5, "unit":'tsp.'},
    "Tortillas":{"quantity":2, "unit":'pieces'},
    "Basil Leaves":{"quantity":6, "unit":'pieces'},
    "Red Onions":{"quantity":0.5, "unit":'pieces'},
    "Arugula Leaves":{"quantity":75, "unit":'g'},
    },
    "Maple Tamarind Glazed Salmon":{
    "Tamarind Paste":{"quantity":4, "unit":'tbsp.'},
    "Maple Syrup":{"quantity":3, "unit":'tbsp.'},
    "Grated Ginger":{"quantity":1, "unit":'tsp.'},
    "Chilli Flakes":{"quantity":1, "unit":'pinch'},
    "Chinese Five Spice":{"quantity":0.5, "unit":'tsp.'},
    "Salt":{"quantity":1, "unit":'pinch'},
    "Black Pepper":{"quantity":1, "unit":'pinch'}
    },
    "Basically Spaghetti Pomodoro":{
    "Canned Tomatoes":{"quantity":400, "unit":'g'},
    "Garlic":{"quantity":4, "unit":'cloves'},
    "Olive Oil":{"quantity":3, "unit":'tbsp.'},
    "Chilli Flakes":{"quantity":1, "unit":'pinch'},
    "Basil Leaves":{"quantity":10, "unit":'pieces'},
    "Dried Spaghetti":{"quantity":450, "unit":'g'},
    "Parmesan":{"quantity":150, "unit":'g'},
    "Butter":{"quantity":2, "unit":'tbsp.'},
    "Salt":{"quantity":3, "unit":'tbsp.'},
    },
    "Blueberry Coffee Cake":{
    "Cream Cheese":{"quantity":350, "unit":'g'},
    "Sugar":{"quantity":375, "unit":'g'},
    "Eggs":{"quantity":3, "unit":'pieces'},
    "Lemon Juice":{"quantity":1, "unit":'tbsp.'},
    "Vanilla":{"quantity":3, "unit":'tsp.'},
    "Butter":{"quantity":55, "unit":'g'},
    "Flour":{"quantity":900, "unit":'g'},
    "Baking Powder":{"quantity":2, "unit":'tbsp.'},
    "Milk":{"quantity":250, "unit":'ml'},
    "Blueberries":{"quantity":700, "unit":'g'},
    },
    "Chocolate Cake":{
    "Butter":{"quantity":125, "unit":'g'},
    "Sugar":{"quantity":500, "unit":'g'},
    "Eggs":{"quantity":2, "unit":'pieces'},
    "Cocoa":{"quantity":5, "unit":'tbsp.'},
    "Salt":{"quantity":0.5, "unit":'tsp.'},
    "Sour Milk":{"quantity":100, "unit":'ml'},
    "Baking Powder":{"quantity":2, "unit":'tsp.'},
    "Flour":{"quantity":500, "unit":'g'},
    "Cloves":{"quantity":0.5, "unit":'tsp.'},
    "Vanilla":{"quantity":1, "unit":'tsp.'},
    },
    "Crazy Cake":{
    "Lemon Cake Mix":{"quantity":500, "unit":'g'},
    "Lemon Jello":{"quantity":1, "unit":'piece'},
    "Vegetable Oil":{"quantity":50, "unit":'ml'},
    "Eggs":{"quantity":4, "unit":'pieces'},
    "Sugar":{"quantity":450, "unit":'g'},
    "Lemon Juice":{"quantity":125, "unit":'ml'},
    },
    "Fresh Apple Cake":{
    "Apples":{"quantity":900, "unit":'g'},
    "Sugar":{"quantity":450, "unit":'g'},
    "Nuts":{"quantity":200, "unit":'g'},
    "Eggs":{"quantity":2, "unit":'pieces'},
    "Vanilla":{"quantity":2, "unit":'tsp.'},
    "Flour":{"quantity":450, "unit":'g'},
    "Baking Powder":{"quantity":2, "unit":'tsp.'},
    "Cinnamon":{"quantity":2, "unit":'tsp.'},
    "Vegetable Oil":{"quantity":100, "unit":'ml'},
    "Baking Soda":{"quantity":1, "unit":'tsp.'},
    "Salt":{"quantity":1, "unit":'tsp.'},
    },
    "Fresh Pear Cake":{
    "Butter":{"quantity":2, "unit":'tbsp.'},
    "Flour":{"quantity":400, "unit":'g'},
    "Pears":{"quantity":3, "unit":'pieces'},
    "Eggs":{"quantity":2, "unit":'pieces'},
    "Sugar":{"quantity":200, "unit":'g'},
    "Milk":{"quantity":100, "unit":'ml'},
    "Salt":{"quantity":1, "unit":'pinch'},
    },
    "Graham Cracker Cake":{
    "Butter":{"quantity":100, "unit":'g'},
    "Sugar":{"quantity":200, "unit":'g'},
    "Sour Milk":{"quantity":200, "unit":'ml'},
    "Graham Crackers":{"quantity":32, "unit":'pieces'},
    "Baking Soda":{"quantity":1, "unit":'tsp.'},
    "Nuts":{"quantity":200, "unit":'g'},
    },
    "Hot Water Chocolate Cake":{
    "Butter":{"quantity":100, "unit":'g'},
    "Sugar":{"quantity":450, "unit":'g'},
    "Eggs":{"quantity":2, "unit":'pieces'},
    "Cocoa":{"quantity":5, "unit":'tbsp.'},
    "Salt":{"quantity":0.5, "unit":'tsp.'},
    "Sour Milk":{"quantity":100, "unit":'ml'},
    "Baking Soda":{"quantity":2, "unit":'tsp.'},
    "Flour":{"quantity":500, "unit":'g'},
    "Cloves":{"quantity":0.5, "unit":'tsp.'},
    "Vanilla":{"quantity":1, "unit":'tsp.'},
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
    "SO GOOD": {"rating": 5, "comment_body": "This is like cocaine for my tastebuds I cannot get enough please send help", "user": user2, "recipe":"Welsh Rarebit"},
    "Not good": {"rating": 2, "comment_body": "This gave me diarrhea", "user": user3, "recipe":"Basically Spaghetti Pomodoro"},
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
    i = Ingredient.objects.get_or_create(name=name, type=type)[0]
    i.save()
    return i

# adding the recipe
def add_recipe(title, servings, category, cooking_time, direction, user, picture):
    r = Recipe.objects.get_or_create(category=category, title=title, servings = servings, cooking_time = cooking_time, direction = direction, user = user, picture=picture)[0]
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
def add_profile(user, picture, about):
    p = UserProfile.objects.get_or_create(user = user, about=about, picture = picture)[0]
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
