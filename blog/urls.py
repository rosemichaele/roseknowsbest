from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.blog_index, name='blog-index'),
]