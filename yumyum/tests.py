from django.test import TestCase
from yumyum.models import Category, Recipe, Type, Ingredient, RecipeIngredient, Review
from yumyum.forms import RecipeIngredientForm,RecipeForm,ReviewForm,ContactForm,UserProfileForm
from datetime import datetime
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from django.urls import reverse

## Testing the model.

class CategoryMethodTests(TestCase):

    # Ensure name cannot repeat
    def test_ensure_unique(self):
        first = Category.objects.create(name='cat1')
        with self.assertRaises(IntegrityError):
            Category.objects.create(name='cat1')

    # Ensure str returns the title
    def test_return_title(self):
        first = Category.objects.create(name='cat1')
        self.assertEqual(str(first), first.name)

    # Ensure number of recipes in cat function works
    def test_number_of_recipes(self):
        category = Category.objects.create(name='cat')
        user1 = User.objects.create(username = "user1", email="myemail@email.com")
        rec1 = Recipe.objects.create(title = "My First Recipe", servings = 1, category = category, cooking_time = 30, direction = "my direction 1", user = user1 )
        rec2 = Recipe.objects.create(title = "My Second Recipe", servings = 1, category = category, cooking_time = 30, direction = "my direction 2", user = user1 )
        rec3 = Recipe.objects.create(title = "My Third Recipe", servings = 1, category = category, cooking_time = 30, direction = "my direction 3", user = user1 )
        recnumber = category.num_of_recipes()
        self.assertEqual(recnumber, 3)

class TypeMethodTests(TestCase):
    # Ensure type is unique
    def test_ensure_unique(self):
        type = Type.objects.create(name='mytype')
        with self.assertRaises(IntegrityError):
            Type.objects.create(name='mytype')

    # Ensure the number of ingredients function works
    def test_number_of_ingredients(self):
        type = Type.objects.create(name='type')
        ing1 = Ingredient.objects.create(name='ing1', type=type)
        ing2 = Ingredient.objects.create(name='ing2', type=type)
        ing3 = Ingredient.objects.create(name='ing3', type=type)
        ingnumber = type.num_of_ingredients()
        self.assertEqual(ingnumber, 3)

    # Ensure str returns the title
    def test_return_title(self):
        first = Type.objects.create(name='type')
        self.assertEqual(str(first), first.name)

class IngredientMethodTests(TestCase):
    # Ensure the name of the ingredient is unique regardless of its type
    def test_ensure_unique_name(self):
        type = Type.objects.create(name='type')
        type2 = Type.objects.create(name='type2')
        ingredient = Ingredient.objects.create(name='bacon', type=type)
        with self.assertRaises(IntegrityError):
            Ingredient.objects.create(name='bacon', type=type2)


class RecipeMethodTests(TestCase):

    # Ensure slug works correctly
    def test_slug_is_right(self):
        user1 = User.objects.create(username = "user1", email="myemail@email.com")
        category1 = Category.objects.create(name = "mycategory")
        recipe1 = Recipe.objects.create(title = "My First Recipe", servings = 1, category = category1, cooking_time = 30, direction = "my direction", user = user1 )
        self.assertEqual(recipe1.slug, 'my-first-recipe')

    # Ensure title of recipe is unique
    def test_unique_title(self):
        user1 = User.objects.create(username = "user1", email="myemail@email.com")
        category1 = Category.objects.create(name = "mycategory")
        recipe1 = Recipe.objects.create(title = "My First Recipe", servings = 1, category = category1, cooking_time = 30, direction = "my direction", user = user1 )
        with self.assertRaises(IntegrityError):
            Recipe.objects.create(title = "My First Recipe", servings = 5, category = category1, cooking_time = 45, direction = "my direction 2", user = user1 )

    # Ensure serving size is not some weird number
    def test_servings_is_sensible(self):
        user1 = User.objects.create(username = "user1", email="myemail@email.com")
        category1 = Category.objects.create(name = "mycategory")
        with self.assertRaises(ValidationError):
            recipe1 = Recipe.objects.create(title = "My Eighth Recipe", servings = -20, category = category1, cooking_time = 30, direction = "my direction", user = user1 )
            recipe1.full_clean()

class ReviewMethodTests(TestCase):

    # Ensure rating number is within tange: 1-5
    def test_rating_is_sensible(self):
        user1 = User.objects.create(username = "user1", email="myemail@email.com")
        category1 = Category.objects.create(name = "mycategory")
        recipe1 = Recipe.objects.create(title = "My Eighth Recipe", servings = 1, category = category1, cooking_time = 30, direction = "my direction", user = user1 )
        with self.assertRaises(ValidationError):
            review1 = Review.objects.create(rating = 7, comment_title="mytitle", comment_body= "i am commenting", user = user1, recipe=recipe1, active = True)
            review1.full_clean()
