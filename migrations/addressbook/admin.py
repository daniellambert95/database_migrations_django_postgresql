from django.contrib import admin
from .models import Address

# Register your models here.


# admin.site.register(Address)

@admin.register(Address)
class addressAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'address')