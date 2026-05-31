from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('add/cake', views.add_cake, name='add_cake')
]