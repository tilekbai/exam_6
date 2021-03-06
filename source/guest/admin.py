from django.contrib import admin
from guest.models import Guestbook

# Register your models here.


class GuestbookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'text', 'status', 'create_time', 'update_time']
    list_filter = ['name', 'status']
    search_fields = ['name', 'status']
    fields = ['name', 'email', 'text', 'status']


admin.site.register(Guestbook, GuestbookAdmin)
