from django.contrib import admin
from guest.models import Guestbook

# Register your models here.


class GuestbookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'text', 'status', 'create_time', 'update_time']
    list_filter = ['name', 'status']
    search_fields = ['name', 'status']
    fields = ['name', 'text', 'status']


admin.site.register(Guestbook, GuestbookAdmin)
