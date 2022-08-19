from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('booking', views.booking, name='booking'),
    path('restaurant', views.restaurant, name='restaurant'),
    path('menu', views.menu, name='menu'),
]
