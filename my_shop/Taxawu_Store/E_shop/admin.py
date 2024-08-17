from django.contrib import admin
from .models import Produit, Categorie, Panier,  Commande

# Register your models here.
admin.site.register(Produit)
admin.site.register(Categorie)
admin.site.register(Panier)

admin.site.register(Commande)
