from django.contrib import admin

from .models import *

# Register your models here.
@admin.register(Baker)
class BakerAdmin(admin.ModelAdmin):
    list_display = ["name", "surname", "phone", "email"]



@admin.register(Cake)
class CakeAdmin(admin.ModelAdmin):
    list_display = ["name", "baker", "price", "weight"]

