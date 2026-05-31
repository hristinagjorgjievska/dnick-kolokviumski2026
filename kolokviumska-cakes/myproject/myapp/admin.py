from django.contrib import admin
from django.db.models import Count

from .models import *

# Register your models here.
@admin.register(Baker)
class BakerAdmin(admin.ModelAdmin):
    ...

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs.annotate(cake_count=Count('cakes')).filter(cake_count__lt=5)

        return qs

@admin.register(Cake)
class CakeAdmin(admin.ModelAdmin):
    ...

    def has_change_permission(self, request, obj=None):
        if obj is None or request.user == obj.baker.user:
            return True
        return False


    def has_view_permission(self, request, obj=None):
        return True

