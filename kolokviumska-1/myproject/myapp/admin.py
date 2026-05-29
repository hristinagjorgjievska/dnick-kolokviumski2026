from django.contrib import admin
from .models import *


@admin.register(Baker)
class BakerAdmin(admin.ModelAdmin):
    list_display = ["name", "surname", "phone", "email"]

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

@admin.register(Cake)
class CakeAdmin(admin.ModelAdmin):
    list_display = ["name", "baker", "price", "weight"]

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True

        if obj is None:
            return True

        return obj.baker.user and obj.baker.user == request.user