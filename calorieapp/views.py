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
    return redirect('list_food')

#view a list of all food items added
def list_all_food_items(request):
    food_items = Food.objects.all()
    total_calories = 0
    for item in food_items:
        total_calories += item.calories
        total_calories = total_calories
    return render(request, 'index.html', {'food_items': food_items, 'total_calories': total_calories})


#remove food items, preferably on at a time
def remove_food_item(request):
    if request.method == 'POST':
        food_id = request.POST.get('food_id')
        food = Food.objects.get(id=food_id)
        food.delete()
    return redirect('list_food')

# calculate and display the total number of calories consumed, maybe add date
# def total_calories(request):
#     food_items = Food.objects.all()
#     total_calories = 0
#     for item in food_items:
#         total_calories += item.calories
#         total_calories = total_calories
#     return render (request, 'index.html', {'total_calories': total_calories})
#render issues