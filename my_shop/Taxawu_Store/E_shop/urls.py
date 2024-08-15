from django.urls import path
from E_shop import views

urlpatterns = [
    path('', views.home, name='shop.html'),
]