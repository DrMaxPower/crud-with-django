from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Booking, Menu


@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):
    """ Staff booking table for costumers manual through admin """
    list_display = ('fname', 'lname', 'date')
    search_fields = ['fname', 'lname', 'email']
    list_filter = ('guests', 'date')
    summmernote_fields = ('info',)


@admin.register(Menu)
class MenuAdmin(SummernoteModelAdmin):
    """  """
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
    list_filter = ('type',)




