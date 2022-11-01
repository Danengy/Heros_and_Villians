from django.urls import path 
from . import views 

urlpatterns = [
    path('<int:pk>/', views.supers_detail),
    path('', views.heroes_villians),
    ]