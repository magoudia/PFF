from django.shortcuts import render
from .models import Produit



# Create your views here.
def home(request,*args,**kwargs):
    """Renders the home page."""
    return render(request,'shop.html')

# pour afficher la liste des produits
def liste_produit (request):
    produits = Produit.objects.all() # Récupère tous les produits de la base de données
    return render(request, 'products/liste_produits.html', {'produits': produits})  # Rend la page HTML avec les produits

# pour afficher les détails d'un produit spécifique
def detail_produit(request, pk):
    produit = Produit.objects.get(pk=pk)  # Récupère le produit correspondant à la clé primaire (pk)
    return render(request, 'products/detail_produit.html', {'produit': produit})  # Rend la page HTML avec les détails du produit