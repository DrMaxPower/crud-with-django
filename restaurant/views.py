from django.shortcuts import render 
from django.views import generic, View
from .models import Booking
from .forms import BookingForm


def home(request):
    all_booking = Booking.objects.order_by('date').all
    return render(request, 'index.html', {'all':all_booking})


def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request, 'booking.html', {})
    else:
        return render(request, 'booking.html', {})
