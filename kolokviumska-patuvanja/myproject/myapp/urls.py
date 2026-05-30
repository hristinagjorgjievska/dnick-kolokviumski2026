from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('add/destination', views.add_destination, name='add_destination')
]