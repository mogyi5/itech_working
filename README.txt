THE INTERNET TECHNOLOGY PROJECT OF ADAMOS S., XINYU X. AND REKA S. FOR AN MSC IN SOFTWARE DEVELOPMENT

*************************IF POPULATE_YUMYUM.PY DOES NOT WORK, DELETE DB.SQLITE3 FILE***************************

TO RUN AFTER PULLING: 

  pip install -r requirements.txt	
  python manage.py makemigrations
  python manage.py migrate
  python populate_yumyum.py
  python manage.py runserver
  
CONTACT FORM ONLY SENDS EMAILS THROUGH THE PYTHONANYWHERE WEBSITE - mailgun does not like us sharing the keys and passwords on github. Proof of working can be acquired from Reka/mogyi5.

THE PROJECT NAME IS: yumyum  <-------------------------------------------------------
THE SUPERUSER DETAILS CAN BE CHANGED IN: populate_yumyum.py

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
  Index  ----------------------www.yumyum.com/yumyum/index/
  Let’s cook ------------------www.yumyum.com/yumyum/cook/
  Search results --------------www.yumyum.com/yumyum/result/
  Recipe pages ----------------www.yumyum.com/yumyum/recipe/{recipe_name}/
  Log in ----------------------www.yumyum.com/yumyum/login/
  Sign up ---------------------www.yumyum.com/yumyum/register/
  Copyright -------------------www.yumyum.com/yumyum/copyright/
  Privacy policy---------------www.yumyum.com/yumyum/policy/
  Upload recipe--------------- www.yumyum.com/yumyum/add_recipe/
  Profile ---------------------www.yumyum.com/yumyum/profile/{user_name}/
