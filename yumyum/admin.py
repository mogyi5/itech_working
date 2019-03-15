#Things to do:
# 1. Group recipeingredients by recipe
# 2. Make it prettier
# 3. Have the recipe and recipeingredient related somehow?

from django.contrib import admin
from yumyum.models import Category, Type, Ingredient, Recipe, RecipeIngredient, Review
from yumyum.models import UserProfile

class RecipeAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('title',)}

class RecipeIngredientAdmin(admin.ModelAdmin):
	list_display = ('recipe', 'ingredient', 'quantity', 'unit')

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
admin.site.register(Category)
admin.site.register(Type)
admin.site.register(Review)
admin.site.register(UserProfile)

# Register your models here.


# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email', 'post', 'created', 'active')
#     list_filter = ('active', 'created', 'updated')
#     search_fields = ('name', 'email', 'body')
# admin.site.register(Comment, CommentAdmin)
