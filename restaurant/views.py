from django.shortcuts import render, redirect 
from .models import Booking
from .forms import BookingForm
from django.contrib import messages



def home(request):
    all_booking = Booking.objects.order_by('date').all
    return render(request, 'index.html', {'all':all_booking})


def restaurant(request):
    return render(request, 'restaurant.html', {})


def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            guests = request.POST['guests']
            date = request.POST['date']
            info = request.POST['info']
            messages.success(request,
            ('You need set name and time for booking to complete.'))
            return render(request, 'booking.html', {
                'fname': fname,
                'lname': lname,
                'email': email,
                'guests': guests,
                'date': date,
                'info': info,
            })
        messages.success(request,
            ('Booking a table was successfully submitted.'))
        return redirect('restaurant')
    else:
        return render(request, 'booking.html', {})
