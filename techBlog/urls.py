# blog/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('<int:post_id>/', index, name='index'),
    path('author/', author, name='author'),
    path('category1/', category1, name='category1'),
    path('category2/', category2, name='category2'),
    path('category3/', category3, name='category3'),
    path('contact/', contact, name='contact'),
    path('single/', single, name='single'),
    path('single/<int:post_id>/', single_post, name='single_post'),
    path('single_news/<int:news_id>/', single_news, name='single_news'),
    path('contact_form/', contact_form, name='contact_form'),

   
]
