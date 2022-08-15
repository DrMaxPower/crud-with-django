from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('booking_table', views.booking_table, name='booking_table'),
    path('staff', views.staff, name='staff'),
]