from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login",views.login_view,name="login"),
    path("logout",views.logout_view,name="logout"),
    path("register",views.register, name="register"),
    path("user",views.user, name="user"),
    path("get_cart",views.get_cart,name="get_cart"),
    path("place_order",views.place_order,name="place_order"),
    path("add_to_cart",views.add_to_cart,name="add_to_cart"),
    path("remove_from_cart",views.remove_from_cart,name="remove_from_cart"),
    path("add_topping",views.add_topping,name="add_topping")
    
    
]
