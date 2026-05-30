from django.contrib import admin
from django.db.models import Count

from .models import *

# Register your models here.
@admin.register(TourGuide)
class TourGuideAdmin(admin.ModelAdmin):
    list_display = ["name", "surname", "phone_number", "email"]

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
            return qs.annotate(travel_count=Count('travel')).filter(travel_count__lt=3)
        return qs

@admin.register(Travel)
class TravelAdmin(admin.ModelAdmin):
    list_display = ["destination", "price", "duration", "tour_guide"]

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser or hasattr(request.user, 'tourguide'):
            return True

        return False


    def has_change_permission(self, request, obj=None):
        if obj is None:
            return True

        if request.user.is_superuser:
            return True

        if request.user == obj.tour_guide.user:
            return True

        return False

    def has_view_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        if obj is None:
            return True

        if request.user.is_superuser:
            return True

        if request.user == obj.tour_guide.user:
            return True

        return False










