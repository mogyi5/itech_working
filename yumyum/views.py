from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from yumyum.models import Category,Type,Ingredient,Recipe,RecipeIngredient,Review, UserProfile
from yumyum.forms import RecipeIngredientForm,RecipeForm,ReviewForm,ContactForm,UserForm,UserProfileForm
from datetime import datetime
from django.contrib.auth.models import User
from django.shortcuts import redirect

def index(request):
    request.session.set_test_cookie()
    context_dict = {}

    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']

    response = render(request, 'yumyum/index.html', context_dict)

    return response

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print(form.errors)
    return render(request, 'yumyum/contact.html', {'form': form})

def cook(request):
    context_dict = {}
    return render(request, 'yumyum/cook.html',context_dict)

def show_recipe(request, recipe_title_slug):
    context_dict = {}

    try:
    	recipe = Recipe.objects.get(slug=recipe_title_slug)
    	context_dict['recipe'] = recipe
    except Recipe.DoesNotExist:
    	context_dict['recipe'] = None

    return render(request, 'yumyum/recipe.html', context_dict)


def add_recipe(request):
    if request.method == 'POST':
        ri_form = RecipeIngredientForm(data=request.POST)
        recipe_form = RecipeForm(data=request.POST)

        if ri_form.is_valid() and recipe_form.is_valid():
            recipe = recipe_form.save(commit=False)
            if 'picture' in request.FILES:
                recipe.picture = request.FILES['picture']
            title = recipe_form.cleaned_data['title']
            cooking_time = recipe_form.cleaned_data['cooking_time']
            direction = recipe_form.cleaned_data['direction']
            recipe.save()
            ri = ri_form.save(commit=False)
            ri.recipe = recipe
            ri.save()

        else:
            print(ri_form.errors, recipe_form.errors)
    else:
        ri_form = RecipeIngredientForm()
        recipe_form = RecipeForm()
    return render(request, 'yumyum/add_recipe.html', {'ri_form': ri_form,
               'recipe_form': recipe_form})

def privacy(request):
    context_dict = {}
    return render(request, 'yumyum/privacy.html',context_dict)

def terms(request):
    context_dict = {}
    return render(request, 'yumyum/terms.html',context_dict)

@login_required
def profile(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return redirect('index')

    userprofile = UserProfile.objects.get_or_create(user=user)[0]
    form = UserProfileForm({'about': userprofile.about, 'picture': userprofile.picture})

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=userprofile)
        if form.is_valid():
            form.save(commit=True)
            return redirect('profile', user.username)
        else:
            print(form.errors)

    return render(request, 'yumyum/profile.html', {'userprofile': userprofile, 'selecteduser': user, 'form': form})

# def search(request):
#     result_list = []
#     if request.method == 'POST':
#         query = request.POST['query'].strip()
#         if query:
#              # Run our Webhose function to get the results list!
#              result_list = run_query(query)
#     return render(request, 'yumyum/search.html', {'result_list': result_list})

# def add_review(request, recipe_title_slug):
#     try:
#         recipe = Recipe.objects.get(slug=recipe_title_slug)
#     except Recipe.DoesNotExist:
#         recipe = None
#     form = ReviewForm(request.POST)
#     if form.is_valid():
#         rating = form.cleaned_data['rating']
#         comment_title = form.cleaned_data['comment_title']
#         comment_body = form.cleaned_data['comment_body']
#         review = Review()
#         review.recipe = recipe
#         review.user_name = user
#         review.rating = rating
#         review.comment_title = comment_title
#         review.comment_body = comment_body
#         review.pub_date = datetime.datetime.now()
#         review.save()
#         return HttpResponseRedirect(reverse('show_recipe', args=(recipe.title,)))
#
#     return render(request, 'yumyum/review.html', {'recipe': recipe, 'form': form})

def visitor_cookie_handler(request):
    visits = int(get_server_side_cookie(request, 'visits', '1'))
    last_visit_cookie = get_server_side_cookie(request,'last_visit',str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7],'%Y-%m-%d %H:%M:%S')
    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1
        request.session['last_visit'] = str(datetime.now())
    else:
        request.session['last_visit'] = last_visit_cookie
    request.session['visits'] = visits

def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val

def get_recipe_list(max_results=0, start_with=''):
    cat_list = []
    if starts_with:
        cat_list = Recipe.objects.filter(name__istartswith=starts_with)

    if max_results > 0:
        if len(cat_list) > max_results:
            cat_list = cat_list[:max_results]
    return cat_list

def suggest_recipe(request):
    cat_list = []
    starts_with = ''

    if request.method == 'GET':
        starts_with = request.GET['suggestion']
    cat_list = get_recipe_list(8, starts_with)

    return render(request, 'yumyum/cats.html', {'cats': cat_list })
