from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

#need a category class for recipe?
#need a type class for ingredient?

class Recipe(models.Model):
	SERVINGS = (
	 ('1','one'),
	 ('2','two'),
	 ('3','three'),
	 ('4','four'),
	 ('5','five'),
	 ('6','six'),
	)
	#picture = models.ImageField(upload_to='recipe_images', blank = True)
	title = models.CharField(max_length=128)
	servings = models.IntegerField(choices=SERVINGS)
	#category = models.ManyToManyField(Category, on_delete=models.PROTECT)
	cooking_time = models.IntegerField(default=60) #in minutes
	direction = models.TextField(max_length=1000)
	slug = models.SlugField(unique=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Recipe, self).save(*args, **kwargs)

	def __str__(self):
		return self.title

class Ingredient(models.Model):
	name = models.CharField(max_length=128)
	quantity = models.CharField(max_length=128)
	type = models.CharField(max_length=32)

	def __str__(self):
		return self.name

class Review(models.Model):
	RATINGS = (
		('1','one'),
		('2','two'),
		('3','three'),
	 	('4','four'),
		('5','five'),
	)
	rating = models.IntegerField(choices=RATINGS)
	comment_title = models.CharField(max_length=100)
	comment_body = models.TextField(max_length=1000)
	#have to also add the user

	def __str__(self):
		return self.comment_title

class UserProfile(models.Model):
	user = models.OneToOneField(User)

	about = models.TextField(max_length = 500) #a short story about yourself, maybe?
	picture = models.ImageField(upload_to='profile_images', blank = True)
	# country

	def __str__(self):
		return self.user.username

#OURS ABOVE
#------------------------------------------------
#RANGO BELOW
# class Category(models.Model):
# 	name = models.CharField(max_length=128, unique=True)
# 	views = models.IntegerField(default=0)
# 	likes = models.IntegerField(default=0)
# 	slug = models.SlugField(unique=True)
#
# 	def save(self, *args, **kwargs):
# 		self.slug = slugify(self.name)
# 		super(Category, self).save(*args, **kwargs)
#
# 	class Meta:
# 		verbose_name_plural = 'categories'
#
# 	def __str__(self):
# 		return self.name
#
# class Page(models.Model):
# 	category = models.ForeignKey(Category)
# 	title = models.CharField(max_length=128)
# 	url = models.URLField()
# 	views = models.IntegerField(default=0)
#
# 	def __str__(self):
# 		return self.title
#
# class UserProfile(models.Model):
# 	user = models.OneToOneField(User)
#
#
# 	website = models.URLField(blank=True)
# 	picture = models.ImageField(upload_to='profile_images', blank = True)
#
# 	def __str__(self):
# 		return self.user.username
