from django.urls import path
from .views import *


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contact.asp', contact, name='contact'),
    path('pricing/', pricing, name='pricing'),
    path('about/', about, name='about'),
    path('connect/', connect, name='connect'),
    path('connect/?search=<keyword>', connect, name='search_results'),
    path('connect/<slug>/', category, name='category'),
    path('connect/<category>/<slug>/', sub_category, name='sub category'),
    path('agency/<slug>/', agency, name='agency'),
    path('store/', search, name='find agency'),
]
