from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):
    """ Staff booking table for costumers manual through admin """
    list_filter = ('guests', 'date')
    summmernote_fields = ('info',)

