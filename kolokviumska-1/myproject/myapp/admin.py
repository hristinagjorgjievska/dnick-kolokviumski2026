from django.contrib import admin

from .models import *

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["name", "surname", "phone", "email"]

@admin.register(Cake)
class CakeAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "weight"]

    def has_change_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            return True
        return False

