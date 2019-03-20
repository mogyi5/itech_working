from django.conf.urls import url
from yumyum import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^cook/', views.cook, name='cook'),
    url(r'^privacy/', views.privacy, name='privacy'),
    url(r'^terms/', views.terms, name='terms'),
    url(r'^profile/(?P<username>[\w\-]+)/$', views.profile, name='profile'),
    url(r'^results/$', views.search, name='search'),
    url(r'^recipe/(?P<recipe_title_slug>[\w\-]+)/$', views.show_recipe, name='show_recipe'),
    url(r'^add_recipe/$', views.add_recipe, name='add_recipe'),
    url(r'^suggest2/$', views.suggest_recipe2, name='suggest_recipe2'),

]
