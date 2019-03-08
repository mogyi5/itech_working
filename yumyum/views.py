from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from rango.models import Category,Type,Ingredient,Recipe,RecipeIngredient,Review
from rango.forms import RecipeIngredientForm,RecipeForm,ReviewForm,ContactForm,UserForm,UserProfileForm
from datetime import datetime

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
    return render(request, 'yumyum/add_category.html', {'form': form})

def cook(request):
    context_dict = {}
    return render(request, 'yumyum/cook.html',context_dict)

def show_recipe(request, title):
    context_dict = {}

    try:
    	recipe = Recipe.objects.get(title=title)
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
    form = UserProfileForm({'website': userprofile.website, 'picture': userprofile.picture})
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=userprofile)
        if form.is_valid():
            form.save(commit=True)
            return redirect('profile', user.username)
        else:
            print(form.errors)
    
    return render(request, 'yumyum/user_profile.html', {'userprofile': userprofile, 'selecteduser': user, 'form': form})

def search(request):
    result_list = []
    if request.method == 'POST':
        query = request.POST['query'].strip()
        if query:
             # Run our Webhose function to get the results list!
             result_list = run_query(query)
    return render(request, 'rango/search.html', {'result_list': result_list})

def add_review(request, title):
    try:
        recipe = Recipe.objects.get(title=title)
    except Recipe.DoesNotExist:
        recipe = None
    form = ReviewForm(request.POST)
    if form.is_valid():
        rating = form.cleaned_data['rating']
        comment_title = form.cleaned_data['comment_title']
        comment_body = form.cleaned_data['comment_body']
        review = Review()
        review.recipe = recipe
        review.user_name = user
        review.rating = rating
        review.comment_title = comment_title
        review.comment_body = comment_body
        review.pub_date = datetime.datetime.now()
        review.save()
        return HttpResponseRedirect(reverse('show_recipe', args=(recipe.title,)))

    return render(request, 'yumyum/review.html', {'recipe': recipe, 'form': form})

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