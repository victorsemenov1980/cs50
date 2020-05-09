from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=64)
    toppings = models.IntegerField()
    size = models.CharField(max_length=1)
    price= models.FloatField()

    def __str__(self):
        return f"{self.name} size {self.size} with ({self.toppings}) toppings at the price of {self.price}"

class Toppings(models.Model):
    name = models.CharField(max_length=64)
    def __str__(self):
        return f"{self.name}"
    
class Order(models.Model):
    username=models.ForeignKey(User, on_delete=models.PROTECT)
    orders=models.ManyToManyField(Menu,blank=True,related_name="food")
    toppings=models.ManyToManyField(Toppings,blank=True,related_name="toppings")
    completion=models.BooleanField(default=False)
    confirmed=models.BooleanField(default=False)

    def __str__(self):
        return  f"{self.username}, completed={self.completion}, confirmed={self.confirmed}"

