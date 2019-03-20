from django.shortcuts import render, redirect
from django.forms.formsets import formset_factory
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from yumyum.models import Category, Type, Ingredient, Recipe, RecipeIngredient, Review, UserProfile
from yumyum.forms import RecipeIngredientForm, RecipeForm, ReviewForm, ContactForm, UserProfileForm
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import IntegrityError, transaction
from yumyum.forms import RIFSet
from django.core.mail import EmailMessage, send_mail
from django.template.loader import get_template
from time import sleep
from django.db.models import Avg, Q
from django.views.generic import ListView


# The view for uploading a recipe - formset factory is used: please be impressed
@login_required
def add_recipe(request):
    user = request.user

    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST, request.FILES)
        ri_formset = RIFSet(request.POST, request.FILES)

        if recipe_form.is_valid() and ri_formset.is_valid():
            # Save user info
            recipe = recipe_form.save(commit=False)
            if 'picture' in request.FILES:
                recipe.picture = request.FILES['picture']
            title = recipe_form.cleaned_data['title']
            cooking_time = recipe_form.cleaned_data['cooking_time']
            direction = recipe_form.cleaned_data['direction']
            recipe.user = user
            recipe.save()

            # Now save the data for each form in the formset
            new_ingredients = []

            for ri in ri_formset:
                ingredient = ri.cleaned_data.get('ingredient')
                quantity = ri.cleaned_data.get('quantity')
                unit = ri.cleaned_data.get('unit')

                if ingredient and quantity and unit:
                    new_ingredients.append(
                        RecipeIngredient(recipe=recipe, ingredient=ingredient, quantity=quantity, unit=unit))

            try:
                with transaction.atomic():
                    # Create new recipeingredients
                    RecipeIngredient.objects.bulk_create(new_ingredients)
                messages.success(request, 'You have added a recipe successfully!')
                sleep(1)
                return redirect(reverse('show_recipe', args=(recipe.slug,)))

            except IntegrityError:  # If the transaction failed
                messages.error(request, 'There was an error adding the recipe.')

    else:
        recipe_form = RecipeForm()
        ri_formset = RIFSet(request.GET or None)

    context_dict = {
        'recipe_form': recipe_form,
        'ri_formset': ri_formset,

    }
    return render(request, 'yumyum/add_recipe.html', context_dict)


def index(request):

    context_dict = {}
    response = render(request, 'yumyum/index.html', context_dict)

    return response

# Contact form should work, if you change the email to your own, you can send yourself emails.
# This is through the API mailgun, it is pretty cool.
def contact(request):
    form_class = ContactForm
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            subject = request.POST.get('subject', '')
            message = request.POST.get('message', '')
            sender = request.POST.get('sender', '')
            send_mail(subject, message, sender, ['szaboki.reka@gmail.com',])


            messages.success(request, 'Your contact form was sent successfully!')
        else:
            messages.warning(request, 'Please correct the error below.')
            print(form.errors)
    return render(request, 'yumyum/contact.html', {'form': form_class})

# The view for showing the recipe.
def show_recipe(request, recipe_title_slug):
    context_dict = {}

    try:
        recipe = Recipe.objects.get(slug=recipe_title_slug)
        ingredients = RecipeIngredient.objects.filter(recipe=recipe)
        reviews = Review.objects.filter(recipe=recipe, active=True).order_by('-rating') # THe recipe reviews.
        current_user = request.user
        if request.user.is_authenticated(): # Count the number of reviews, because the user should only be able to submit one.
            count_revs = Review.objects.filter(recipe=recipe, user=current_user).count()
            intcount = int(count_revs)
            context_dict['intcount'] = intcount
        context_dict['recipe'] = recipe
        context_dict['reviews'] = reviews
        context_dict['recipe_ingredients'] = ingredients
    except Recipe.DoesNotExist:
        return redirect('index')
        context_dict['recipe'] = None
        context_dict['reviews'] = None

    if request.method == 'POST':
        # A comment was posted
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            # Create Comment object but don't save to database yet
            new_review = review_form.save(commit=False)
            # Assign the current post to the comment
            new_review.recipe = recipe
            new_review.user = current_user
            # Save the comment to the database
            new_review.save()
            newr = True
        else:
            print(form.errors)

    else:
        review_form = ReviewForm()
        newr = False

    context_dict['newr'] = newr
    context_dict['review_form'] = review_form

    # Return the average review after each review as well.
    avg_rev = Review.objects.filter(recipe=recipe, active=True).aggregate(Avg('rating'))
    context_dict['avg_rev'] = avg_rev['rating__avg']

    return render(request, 'yumyum/recipe.html', context_dict)

# That's right we have a privacy and a terms page too.
def privacy(request):
    context_dict = {}
    return render(request, 'yumyum/privacy.html', context_dict)


def terms(request):
    context_dict = {}
    return render(request, 'yumyum/terms.html', context_dict)


@login_required
def profile(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return redirect('index')

    recipes = Recipe.objects.filter(user=user)
    userprofile = UserProfile.objects.get_or_create(user=user)[0]
    form = UserProfileForm({'about': userprofile.about, 'picture': userprofile.picture})

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=userprofile)
        if form.is_valid():
            form.save(commit=True)
            return redirect('profile', user.username)
        else:
            print(form.errors)

    return render(request, 'yumyum/profile.html',
                  {'userprofile': userprofile, 'selecteduser': user, 'form': form, 'recipes': recipes})


def get_recipe_list(max_results=0, include_with=''):
    cat_list = []
    if include_with:
        cat_list = Recipe.objects.filter(title__icontains=include_with)

    if max_results > 0:
        if len(cat_list) > max_results:
            cat_list = cat_list[:max_results]
    return cat_list

# Use with the ajax - shows recipe suggestions inline
def suggest_recipe2(request):
    cat_list = []
    include_with = ''

    if request.method == 'GET':
        include_with = request.GET['suggestion2']
    cat_list = get_recipe_list(100, include_with)

    return render(request, 'yumyum/cats.html', {'cats': cat_list})

# The search result shown if searching by ingredient.
def search(request):
    inResult = []
    query = request.GET.get('q')

    if query:
        result = []
        # a list of comma separated values turned into list
        k = [x.strip() for x in query.split(',')]
        for one_ingredient in k:

            try:
                # Search the ingredients by *exact name* to avoid weird results.
                # This however restrcits the search, as if you type 'pear', it will not Return
                # recipes with the ingredient 'pears'
                inResult = Ingredient.objects.get(name__iexact=one_ingredient)
            except:
                inResult = None

            if inResult:
                ri_results = inResult.recipeingredient_set.all()
                for ri in ri_results:
                    results = ri.recipe
                    result.append(results)
        set_result = set(result)
        re = list(set_result)
        # try to sort the output to see most relevant recipes first, by the number of ingredients matching.
        sort_func = lambda recipe: len(
            set(recipe.recipeingredient_set.all().values_list('ingredient', flat=True)) & set(k))
        rec_recipe_list = sorted(re, key=sort_func)

        if len(rec_recipe_list) == 0:
            rec_recipe_list = None


    return render(request, 'yumyum/search_result.html', {'cats': rec_recipe_list})


def cook(request):
    context_dict = {}
    return render(request, 'yumyum/cook.html', context_dict)
