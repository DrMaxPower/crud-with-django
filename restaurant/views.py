from django.shortcuts import render
from .models import Booking

# Create your views here.

def index(request):
    bookings_info = Booking.objects.all()
    return render(request, 'index.html', {'info': bookings_info})

def booking_table(request):
     return render(request, 'booking_table.html', {})


def staff(request):
     return render(request, 'staff.html', {})
