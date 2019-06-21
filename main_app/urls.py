from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.WishCreate.as_view(), name='create'),
    path('<int:pk>/delete/', views.WishDelete.as_view(), name = 'delete'),
]