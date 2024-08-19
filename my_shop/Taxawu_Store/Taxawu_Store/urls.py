"""
URL configuration for Taxawu_Store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path,include

from E_shop import views
from E_shop.views import liste_produit


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('E_shop.urls')),
    path('produits/', liste_produit, name='liste_produit'),
     path('produits/<int:pk>/', views.detail_produit, name='detail_produit'),  # Détails du produit

]
