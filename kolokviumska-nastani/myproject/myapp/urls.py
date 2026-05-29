from . import views
from django.urls import path

urlpatterns = [
    path('index/', views.index, name='index'),
    path('add/event/', views.add_event, name='add_event')
]