from django.contrib import admin
from yumyum.models import Category, Type, Ingredient, Recipe, RecipeIngredient, Review
from yumyum.models import UserProfile

#Displaying and filtering each admin site sensibly.
class RecipeAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'user')
	prepopulated_fields = {'slug':('title',)}
	list_filter = ('category', 'user')

class RecipeIngredientAdmin(admin.ModelAdmin):
	list_display = ('ingredient', 'quantity', 'unit','recipe')
	list_filter = ('recipe',)

class ReviewAdmin(admin.ModelAdmin):
	list_display = ('comment_title', 'recipe', 'rating', 'active')
	list_filter = ('recipe', 'active')

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'num_of_recipes')

class IngredientAdmin(admin.ModelAdmin):
	list_display = ('name', 'type')
	list_filter = ('type',)

class TypeAdmin(admin.ModelAdmin):
	list_display = ('name', 'num_of_ingredients')

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Type,TypeAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(UserProfile)
