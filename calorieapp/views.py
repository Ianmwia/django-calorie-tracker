from django.shortcuts import render, redirect, get_object_or_404
from .models import Food, UserEntry
from django.contrib.auth.models import User
from datetime import date

# Create your views here.
def index(request):
    return render(request ,'index.html' )

#add new food item with calorie count
def add_food(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        calories = request.POST.get('calories')

        # create user
        user = request.user

        food, created = Food.objects.get_or_create(name = name, calories = calories)
        UserEntry.objects.create(user = user,food = food, date = date.today())
    return redirect('list_food')

#view a list of all food items added
def list_all_food_items(request):
    user = request.user
    user_entries = UserEntry.objects.filter(user=user)

    #food_items = Food.objects.all()
    total_calories = 0
    for item in user_entries:
        total_calories += item.calories
        total_calories = total_calories
    return render(request, 'index.html', {'food_items': user_entries, 'total_calories': total_calories})


#remove food items, preferably on at a time
def remove_food_item(request):
    if request.method == 'POST':
        food_id = request.POST.get('food_id')
        #food = Food.objects.get(id=food_id) #http hidden vs <str:int> avoid displaying data to the user and send data to the browser
        #food = get_object_or_404(Food, id=food_id)
        user = request.user
        food = get_object_or_404(UserEntry, user=user, id=food_id)
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

# reset calories count ## need user and date