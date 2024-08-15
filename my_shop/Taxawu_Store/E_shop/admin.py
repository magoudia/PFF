from django.contrib import admin
from .models import Produit, Categorie, Panier, ElementPanier, Commande, ElementCommande, Paiement, Avis, Livraison, Recherche

# Register your models here.
admin.site.register(Produit)
admin.site.register(Categorie)
admin.site.register(Panier)
admin.site.register(ElementPanier)
admin.site.register(Commande)
admin.site.register(ElementCommande)
admin.site.register(Paiement)
admin.site.register(Avis)
admin.site.register(Livraison)
admin.site.register(Recherche)