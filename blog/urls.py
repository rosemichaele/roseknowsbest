from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.BlogIndexView.as_view(), name='blog-index'),
    path('<int:pk>/', views.BlogEntryView.as_view(), name='blog-entry')
]