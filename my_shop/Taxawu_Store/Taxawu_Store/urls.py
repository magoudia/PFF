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
from E_shop.views import liste_produit,liste_commande


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('E_shop.urls')),
    path('produits/', views.liste_produit, name='liste_produit'),
    path('commandes/', liste_commande, name='liste_commande'),
    path('produits/<int:pk>/', views.detail_produit, name='detail_produit'),  # Détails du produit
    path('ajouter_au_panier/<int:produit_id>/', views.ajouter_au_panier, name='ajouter_au_panier'),
    path('mon-compte/', views.mon_compte, name='mon_compte'),
    path('panier/', views.panier, name='panier'),

]
