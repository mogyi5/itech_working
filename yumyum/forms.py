from django import forms
from django.forms import formset_factory
from django.contrib.auth.models import User
from yumyum.models import Ingredient, Recipe, RecipeIngredient, Review, UserProfile

#Maybe done?
#When user makes a new recipe, the form will be recipeingredientform and recipeform together
#because of the nature of the database.
class RecipeIngredientForm(forms.ModelForm):

    class Meta:
        model = RecipeIngredient
        exclude = ('recipe',) # exclude this because it will be added to the current recipe anyway

RIFSet = formset_factory(RecipeIngredientForm, extra = 1)

class RecipeForm(forms.ModelForm):

    picture = forms.ImageField(help_text= "Upload a photo", required = False)
    title = forms.CharField(max_length=128, help_text = "Recipe title", required = True)
    cooking_time = forms.IntegerField(help_text= "Cooking time in minutes", required = True) #in minutes
    direction = forms.CharField(widget=forms.Textarea, max_length=1000, help_text = "Cooking directions", required = True)
    slug = forms.CharField(widget=forms.HiddenInput(), required = False)

    class Meta:
        model = Recipe
        exclude = ('slug', 'user')

class ReviewForm(forms.ModelForm):
    comment_body = forms.CharField(widget=forms.Textarea, max_length=200, help_text = "Add your review here!")

    class Meta:
        model = Review
        exclude = ('recipe', 'active', 'user')

# A form for contact us
# change the sender from emailfield to user maybe
class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea, initial = 'Your message here!')
    sender = forms.EmailField(initial = 'Email address')
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
