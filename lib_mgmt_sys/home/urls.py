from unicodedata import name
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.home, name="home"),
    path('contact/', views.contact, name="contact"),
    path('feature/', views.feature, name="feature"),
    path('add_author', views.add_author, name='add_author'),
    path('add_book', views.add_book, name='add_book'),
    path('edit_book/<int:id>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:id>/', views.delete_book, name='delete_book'),
    path('list_book/', views.list_book, name='list_book'),

]