from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Menu,Toppings,Order
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.db.models import Sum
from collections import OrderedDict




# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, "login.html", {"message": None})
    username=request.user
    user_cart=Order.objects.filter(username=username)
    cart_cost1=Menu.objects.all().filter(food__in=user_cart).aggregate(Sum('price'))
    cart_cost=cart_cost1['price__sum']
    cart=user_cart.count()
    context = {
        "user": request.user,
        "menu":Menu.objects.all(),
        "cart":cart,
        "cart_cost":cart_cost
        
    }
    return render(request, "index.html", context)

def user(request):
    if not request.user.is_authenticated:
        return render(request, "login.html", {"message": None})
    context = {
        "user": request.user,
    }
    return render(request, "user.html", context)

def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("user"))
    else:
        return render(request, "login.html", {"message": "Invalid credentials. Maybe you need to register first"})

def logout_view(request):
    logout(request)
    return render(request, "login.html", {"message": "Logged out."})

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return HttpResponseRedirect(reverse("index"))
    else:
        form = RegisterForm()

    return render(response, "register.html", {"form":form})

def get_cart(request):
    if not request.user.is_authenticated:
        return render(request, "login.html", {"message": None})
    
    username=request.user
    user_cart=Order.objects.filter(username=username)
    cart_cost1=Menu.objects.all().filter(food__in=user_cart).aggregate(Sum('price'))
    cart_cost=cart_cost1['price__sum']
    cart=Menu.objects.all().filter(food__in=user_cart)
    # cart=Menu.objects.all().filter(food__in=user_cart).values('id','name','toppings__name','size','price')
    cart_toppings=Toppings.objects.all().filter(toppings__in=user_cart)
    super_cart=Order.objects.filter(username=username).values('id','orders__name','toppings__name')
    user_cart1=Order.objects.filter(username=username).values('id')
    grouped4={}
    for i in user_cart1.values_list('id',flat=True):
        grouped4.update({i:[]})
    for i in super_cart:  
        grouped=i
        
        if grouped['id']in user_cart1.values_list('id',flat=True):
            grouped4[grouped['id']].append(grouped['toppings__name'])
        
    grouped2=super_cart.values_list('id', flat=True)
    grouped3=user_cart.values_list('id',flat=True)
    
   
    # for i in super_cart:
    #     if super_cart(i)==grouped4(i):
    #         grouped4[i].append(super_cart['toppings__name'])
    new=tuple(zip(user_cart,cart)) 
    
    context = {
        "user": request.user,
        "menu":Menu.objects.all(),
        "cart":cart,
        "cart_cost":cart_cost,
        'n' :Toppings.objects.all(),
        "user_cart":user_cart,
        "new":new,
        "cart_toppings":cart_toppings,
        "super_cart":super_cart,
        'grouped':grouped,
        'grouped2':grouped2,
        'grouped3':grouped3,
        'grouped4':grouped4,
        'new2':grouped['id']
        }
        
        
    return render(request, 'cart.html', context)

def add_to_cart(request):
    food_id = request.POST['food.id']
    username=request.user
    food = Menu.objects.get(id=food_id)
    cart=Order.objects.create(username=username)
    cart.orders.add(food)
   
    return HttpResponseRedirect(reverse("index"))

def remove_from_cart(request):
    element_id = request.POST['element.id']
    username=request.user
    Order.objects.filter(username=username,id=element_id).delete()
    
   
    return HttpResponseRedirect(reverse("get_cart"))

    
def place_order(request):
    if not request.user.is_authenticated:
        return render(request, "login.html", {"message": None})
    username=request.user
    cart =  Order.objects.filter(username=username)
    for item in cart:
        item.confirmed = True
        item.save()
    
    context = {
        "user": request.user,
        
    }
    return render(request, "order_placed.html", context)

def add_topping(request):
    element_id = request.POST['element.id']
    username=request.user
    item=Order.objects.filter(username=username,id=element_id)
    topping_id = request.POST['topping']
    topping=Toppings.objects.get(id=topping_id)
    for x in item:
        x.toppings.add(topping)
    


    return HttpResponseRedirect(reverse("get_cart"))













