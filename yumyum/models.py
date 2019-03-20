from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db.models import Count
from django.core.exceptions import ValidationError

# A category model has just a name, used to identify recipes
class Category(models.Model):
	name = models.CharField(max_length = 32, unique=True)

	class Meta:
		ordering = ['name']
		verbose_name_plural = 'categories'

# A function to help count the number of recipes in a category
	def num_of_recipes(self):
		counter =  Recipe.objects.filter(category = self).annotate(Count("id"))
		return len(counter)
	num_of_recipes.short_description = 'Recipes in Category'

	def __str__(self):
		return self.name


# The same as category, except a type applies to ingredients
class Type(models.Model):
	name = models.CharField(max_length = 32, unique=True)

	class Meta:
		ordering = ['name']

	def num_of_ingredients(self):
		counter =  Ingredient.objects.filter(type = self).annotate(Count("id"))
		return len(counter)
	num_of_ingredients.short_description = 'Ingredients of this Type'

	def __str__(self):
		return self.name

# An ingredient has a name and a type. The name must be unique.
class Ingredient(models.Model):
	name = models.CharField(max_length=32, unique=True)
	type = models.ForeignKey(Type)

	class Meta:
		ordering = ['name']

	def __str__(self):
		return self.name

# A recipe consists of the below attributes.
class Recipe(models.Model):

# A validator to make sure the number of servings and cooking time are sensible.
	def number_positive_validator(value):
		if (value < 0):
			raise ValidationError('%s should not be negative' % value)

	SERVINGS = (
	 (1,'1'),
	 (2,'2'),
	 (3,'3'),
	 (4,'4'),
	 (5,'5'),
	 (6,'6'),
	)
	# picture does not have to be present
	picture = models.ImageField(upload_to='recipe_images', blank = True)
	# unique title
	title = models.CharField(max_length=128, unique=True)
	servings = models.IntegerField(choices=SERVINGS, validators=[number_positive_validator])
	category = models.ForeignKey(Category)
	cooking_time = models.IntegerField(default=30, validators=[number_positive_validator]) #in minutes
	direction = models.TextField(max_length=1500)
	slug = models.SlugField(unique=True)
	user = models.ForeignKey(User) # the user who uploaded the recipe

	class Meta:
		ordering = ['category','title']

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Recipe, self).save(*args, **kwargs)

	def __str__(self):
		return self.title

# A recipeingredient is just an ingredient associated with a recipe. Here we can add the quantity and unit, becasue it's different for every recipe.
class RecipeIngredient(models.Model):
	UNITS = (
	 ('tsp.', 'tsp.'),
	 ('tbsp.', 'tbsp.'),
	 ('ml', 'ml'),
	 ('l', 'l'),
	 ('g','g'),
	 ('kg','kg'),
	 ('pieces', 'pieces'),
	 ('pinch', 'pinch'),
	 ('cloves', 'cloves'),
	 ('slices','slices')
	)
	recipe = models.ForeignKey(Recipe, null = True)
	ingredient = models.ForeignKey(Ingredient, null=True)
	quantity = models.DecimalField(decimal_places=2, max_digits=5,)	#a decimal field because we could have 0.5 lemon for example
	unit = models.CharField(choices = UNITS, max_length=30) # the units have to be from a choice for evenness and imperial measurements suck anyways.

	class Meta:
		ordering = ['recipe']
		unique_together = ('recipe', 'ingredient',)  # one recipe can have one ingredient only once

	def __str__(self):
		return self.ingredient.name

# A review has a title, body, rating (from 1 - 5), the user, recipe and active.
class Review(models.Model):

	def sensible_rating_validator(value):
		if value < 1 or value > 5:
			raise ValidationError('%s should be within range: 1-5' % value)

	RATINGS = (
		(1,'1'),
		(2,'2'),
		(3,'3'),
	 	(4,'4'),
		(5,'5'),
	)
	rating = models.IntegerField(choices=RATINGS, validators=[sensible_rating_validator])
	comment_title = models.CharField(max_length=100)
	comment_body = models.TextField(max_length=1000)
	user = models.ForeignKey(User)
	recipe = models.ForeignKey(Recipe)
	active = models.BooleanField(default=True) # for moderation purposes, if someone is abusive we set active to false and it will not show.

	def __str__(self):
		return self.comment_title

	class Meta:
		ordering = ['recipe','rating']

# A user has username/password etc, as well as an about, and a profile picture.
class UserProfile(models.Model):
	user = models.OneToOneField(User)

	about = models.TextField(max_length = 500) #a short story about yourself
	picture = models.ImageField(upload_to='profile_images', blank = True)

	def __str__(self):
		return self.user.username
