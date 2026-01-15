from django.urls import path
from . import views

urlpatterns = [
    path("index", views.index, name='index'),
    path("add_food/", views.add_food, name='add_food'),
    path("list_food", views.list_all_food_items, name='list_food'),
]

