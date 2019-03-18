from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db.models import Count
from django.core.exceptions import ValidationError

class Category(models.Model):
	name = models.CharField(max_length = 32, unique=True)

	class Meta:
		ordering = ['name']
		verbose_name_plural = 'categories'

	def num_of_recipes(self):
		counter =  Recipe.objects.filter(category = self).annotate(Count("id"))
		return len(counter)
	num_of_recipes.short_description = 'Recipes in Category'

	def __str__(self):
		return self.name


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

class Ingredient(models.Model):
	name = models.CharField(max_length=32, unique=True)
	type = models.ForeignKey(Type)

	class Meta:
		ordering = ['name']

	def __str__(self):
		return self.name

class Recipe(models.Model):

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
	picture = models.ImageField(upload_to='recipe_images', blank = True)
	title = models.CharField(max_length=128, unique=True)
	servings = models.IntegerField(choices=SERVINGS, validators=[number_positive_validator])
	category = models.ForeignKey(Category)
	cooking_time = models.IntegerField(default=30) #in minutes
	direction = models.TextField(max_length=1500)
	slug = models.SlugField(unique=True)
	user = models.ForeignKey(User)

	class Meta:
		ordering = ['category','title']

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Recipe, self).save(*args, **kwargs)

	def __str__(self):
		return self.title

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
	quantity = models.DecimalField(decimal_places=2, max_digits=5,)
	unit = models.CharField(choices = UNITS, max_length=30)

	class Meta:
		ordering = ['recipe']
		unique_together = ('recipe', 'ingredient',)

	def __str__(self):
		return self.ingredient

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
	active = models.BooleanField(default=True)

	def __str__(self):
		return self.comment_title

	class Meta:
		ordering = ['recipe','rating']

class UserProfile(models.Model):
	user = models.OneToOneField(User)

	about = models.TextField(max_length = 500) #a short story about yourself, maybe?
	picture = models.ImageField(upload_to='profile_images', blank = True)

	def __str__(self):
		return self.user.username
