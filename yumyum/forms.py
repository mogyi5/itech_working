from django import forms
from django.contrib.auth.models import User
from yumyum.models import Ingredient, Recipe, RecipeIngredient, Review, UserProfile

#Maybe done?
#When user makes a new recipe, the form will be recipeingredientform and recipeform together
#because of the nature of the database.
class RecipeIngredientForm(forms.ModelForm):

    class Meta:
        model = RecipeIngredient
        exclude = ('recipe',) # exclude this because it will be added to the current recipe anyway

class RecipeForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text = "Please enter a recipe title")
    cooking_time = forms.IntegerField(help_text= "Please enter cooking time in minutes") #in minutes
    direction = forms.CharField(max_length=1000, help_text = "Please enter cooking directions")
    slug = forms.CharField(widget=forms.HiddenInput(), required = False)

    class Meta:
        model = Recipe
        exclude = ('slug',)

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        exclude = ('recipe', 'user')

# A form for contact us
# change the sender from emailfield to user maybe
class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100, initial = 'Subject')
    message = forms.CharField(initial = 'Please enter your message')
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

#make a user
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','email', 'password')

#make a user profile
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('about', 'picture')
