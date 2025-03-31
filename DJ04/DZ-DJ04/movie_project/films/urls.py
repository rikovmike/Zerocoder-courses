from django.urls import path,include
from .views import add_film, film_list

urlpatterns = [
    path('add/', add_film, name='add_film'),
    path('', film_list, name='film_list'),
]