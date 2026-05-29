from django.contrib import admin

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ["name", "surname", "phone", "email"]

class CakeAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "weight"]

    def has_change_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            return True
        return False

