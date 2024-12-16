from django.urls import path
from . import views

urlpatterns = [
    path('cars/', views.car_list, name='car_list'),
    path('associations/', views.association_list, name='association_list'),
    path('owners/', views.owner_list, name='owner_list'),
    path('', views.index, name='index'),
    path('request/', views.request, name='request')
]
