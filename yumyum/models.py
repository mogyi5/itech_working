from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Category(models.Model):
	name = models.TextField(max_length = 32)

	class Meta:
		ordering = ['name']

	def __str__(self):
		return self.name


class Type(models.Model):
	name = models.TextField(max_length = 32)

	class Meta:
		ordering = ['name']

	def __str__(self):
		return self.name

class Ingredient(models.Model):
	name = models.CharField(max_length=32)
	type = models.ForeignKey(Type, null=True)

	class Meta:
		ordering = ['type', 'name']

	def __str__(self):
		return self.name

class Recipe(models.Model):
	SERVINGS = (
	 (1,'1'),
	 (2,'2'),
	 (3,'3'),
	 (4,'4'),
	 (5,'5'),
	 (6,'6'),
	)
	picture = models.ImageField(upload_to='recipe_images', blank = True)
	title = models.CharField(max_length=128)
	servings = models.IntegerField(choices=SERVINGS)
	category = models.ForeignKey(Category)
	cooking_time = models.IntegerField(default=60) #in minutes
	direction = models.TextField(max_length=1000)
	slug = models.SlugField(unique=True)
	user = models.ForeignKey(User)

	class Meta:
		ordering = ['title']

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
	quantity = models.IntegerField()
	unit = models.CharField(choices = UNITS, max_length=30)

	class Meta:
		ordering = ['recipe']

	def __str__(self):
		return self.ingredient

class Review(models.Model):
	RATINGS = (
		(1,'1'),
		(2,'2'),
		(3,'3'),
	 	(4,'4'),
		(5,'5'),
	)
	rating = models.IntegerField(choices=RATINGS)
	comment_title = models.CharField(max_length=100)
	comment_body = models.TextField(max_length=1000)
	user = models.ForeignKey(User)
	recipe = models.ForeignKey(Recipe, null= True)

	def __str__(self):
		return self.comment_title

class UserProfile(models.Model):
	user = models.OneToOneField(User)

	about = models.TextField(max_length = 500) #a short story about yourself, maybe?
	picture = models.ImageField(upload_to='profile_images', blank = True)

	def __str__(self):
		return self.user.username
