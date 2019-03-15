from django.conf.urls import url
from yumyum import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^cook/', views.cook, name='cook'),
    url(r'^privacy/', views.privacy, name='privacy'),
    url(r'^terms/', views.terms, name='terms'),
    url(r'^profile/(?P<username>[\w\-]+)/$', views.profile, name='profile'),
    # url(r'search/$', views.search, name='search'),
    # url(r'^review/', views.review, name='review'),
    url(r'^recipe/(?P<recipe_title_slug>[\w\-]+)/$', views.show_recipe, name='show_recipe'),
    url(r'^add_recipe/$', views.add_recipe, name='add_recipe'),

#    url(r'^login/$', views.user_login, name='login'),
#    url(r'^register/$', views.register, name='register'),

    #url(r'^add_category/$', views.add_category, name='add_category'),
    #url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.show_category, #name='show_category'),
    #url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, #name='add_page'),
    #url(r'^register/$', views.register, name='register'),
    #url(r'^login/$', views.user_login, name='login'),
    #url(r'^restricted/', views.restricted, name='restricted'),
    #url(r'^logout/$', views.user_logout, name='logout'),
]
