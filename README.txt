***********BEFORE YOU PUSH DELETE db.sqlite3 & THE FILES IN yumyum/pycache (except __init__)***************************

TO RUN AFTER PULLING: 

  pip install django-inlinecss - the first time

  python manage.py makemigrations
  python manage.py migrate
  python populate_yumyum.py
  python manage.py runserver

THE PROJECT NAME IS: yumyum
THE SUPERUSER DETAILS CAN BE CHANGED IN: populate_yumyum.py

SEE CURRENT DB LAYOUT IN models.py IT MAY OR MAY NOT BE PERFECT
 TABLES: Type (for an ingredient)
	 Category (for a recipe)
	 Ingredient (all ingredients)
	 Recipe (all recipes)
	 RecipeIngredient (the ingredients in a specific recipe - taking foreign keys from both recipe and ingredient)
	 Reviews (reviews for a recipe from a user)
	 UserProfile (profiles for a user)
	 

PAGES WE CURRENTLY HAVE:
  Homepage --------------------www.yumyum.com
  Contact ---------------------www.yumyum.com/yumyum/contact/
  Sitemap (index) -------------www.yumyum.com/yumyum/index/
  Let’s cook ------------------www.yumyum.com/yumyum/cook/
  Search results --------------www.yumyum.com/yumyum/result/
  Recipe pages ----------------www.yumyum.com/yumyum/recipe/{recipe_name}/
  Log in ----------------------www.yumyum.com/yumyum/login/
  Sign up ---------------------www.yumyum.com/yumyum/register/
  Copyright -------------------www.yumyum.com/yumyum/copyright/
  Privacy policy---------------www.yumyum.com/yumyum/policy/
  Upload recipe--------------- www.yumyum.com/yumyum/add_recipe/
  Account ---------------------www.yumyum.com/yumyum/account/{user_name}/
