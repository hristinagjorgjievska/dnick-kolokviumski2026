from django.contrib import admin

from .models import *

# Register your models here.
@admin.register(Band)
class BandAdmin(admin.ModelAdmin):
    list_display = ["name", "country"]

class BandEventInline(admin.TabularInline):
    model = BandEvent
    extra = 1

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ["name", "date"]
    inlines = [BandEventInline]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super().save_model(request, obj, form, change)

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if obj is None:
            return False

        band_events = BandEvent.objects.filter(event=obj)
        if band_events.count() == 0 and obj.user == request.user:
            return True

        return False

    def has_change_permission(self, request, obj=None):
        if obj is None:
            return False

        band_events = BandEvent.objects.filter(event=obj)
        if band_events.count() == 0 and obj.user == request.user:
            return True

        return False




