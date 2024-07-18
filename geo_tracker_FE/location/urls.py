from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update_location/', views.update_location, name='update_location'),
    path('get_locations/', views.get_locations, name='get_locations'),
]
