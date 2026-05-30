from django.contrib import admin
from django.contrib.auth.models import Permission
from django.core.exceptions import ValidationError
from django.db.models import Sum, Count

from .models import *


@admin.register(Baker)
class BakerAdmin(admin.ModelAdmin):
    list_display = ["name", "surname", "phone", "email"]

    def has_add_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs.annotate(cake_count=Count('cake')).filter(cake_count__lt=5)
        return qs

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if not change:
            user = obj.user
            user.is_staff = True
            cake_permissions = Permission.objects.filter(codename__in=[
                'add_cake', 'change_cake', 'view_cake', 'delete_cake'
            ])
            user.user_permissions.set(cake_permissions)
            user.save()


@admin.register(Cake)
class CakeAdmin(admin.ModelAdmin):
    list_display = ["name", "baker", "price", "weight"]

    def has_view_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        if obj is None:
            return True
        if request.user.is_superuser:
            return True
        return obj.baker.user == request.user

    def save_model(self, request, obj, form, change):
        # Проверка за исто име (само при ново додавање)
        if not change and Cake.objects.filter(name__iexact=obj.name).exists():
            raise ValidationError('Веќе постои торта со тоа име!')

        # Постави baker автоматски ако е обичен пекар
        if not change and not request.user.is_superuser:
            obj.baker = request.user.baker

        # Проверка за вкупна цена
        total_price = Cake.objects.filter(baker=obj.baker).aggregate(total=Sum('price'))['total'] or 0
        if not change and total_price + obj.price > 10000:
            raise ValidationError('Вкупната цена на тортите на пекарот надминува 10 000!')

        super().save_model(request, obj, form, change)