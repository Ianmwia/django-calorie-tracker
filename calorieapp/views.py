from django.shortcuts import render, redirect
from .models import Food

# Create your views here.
def index(request):
    return render(request ,'index.html' )

#add new food item with calorie count
def add_food(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        calories = request.POST.get('calories')
        Food.objects.create(name = name, calories = calories)
    return redirect('index')

