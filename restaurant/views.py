from django.shortcuts import render, redirect 
from .models import Booking, Menu
from .forms import BookingForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def home(request):
    return render(request, 'index.html', {})


@login_required
def restaurant(request):
    all_booking = Booking.objects.order_by('date').all
    return render(request, 'restaurant.html', {'all':all_booking})


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
        return redirect('booking')
    else:
        return render(request, 'booking.html', {})



def menu(request):
    all_menu = Menu.objects.order_by('price').all
    return render(request, 'menu.html', {'menu':all_menu})

