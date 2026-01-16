from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=50)
    calories = models.IntegerField()

class UserEntry(models.Model):
    '''
    Docstring for UserEntry for logging different users into the system
    user - one user can have multiple food entries
    food - a foreign key allows the food to be unique each day to each user
    '''
    user = models.ForeignKey(User, verbose_name=("User"), on_delete=models.CASCADE)
    food = models.ForeignKey(Food, verbose_name=("Food"), on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True, verbose_name=('Date'))