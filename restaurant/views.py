from django.shortcuts import render, redirect
from django.views import generic
from .models import Booking
from .forms import BookingForm


class BookingList(generic.ListView):
    model = Booking
    queryset = Booking.objects.order_by('date')
    template_name = 'index.html'
    paginate_by = 10