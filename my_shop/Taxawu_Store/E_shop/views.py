from Taxawu_Store.E_shop.forms import FormulaireInscription
from django.shortcuts import redirect, render
from .models import Produit
from django.contrib.auth import login, authenticate



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

# Vue pour gérer l'inscription des utilisateurs
def inscription(request):
    if request.method == 'POST':  # Si le formulaire est soumis
        form = FormulaireInscription(request.POST)  # Instancie le formulaire avec les données soumises
        if form.is_valid():  # Vérifie si les données sont valides
            form.save()  # Sauvegarde le nouvel utilisateur
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # Authentifie l'utilisateur
            login(request, user)  # Connecte l'utilisateur
            return redirect('home')  # Redirige vers la page d'accueil
    else:
        form = FormulaireInscription()  # Instancie un formulaire vide
    return render(request, 'users/inscription.html', {'form': form})  # Rend la page d'inscription