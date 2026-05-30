from django.contrib import admin

from .models import *

# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["name", "surname", "email"]

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False



@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["name", "surname", "email"]

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "price"]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super().save_model(request, obj, form, change)

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False
