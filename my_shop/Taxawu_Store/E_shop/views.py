from .forms import FormulaireInscription
from django.shortcuts import redirect, render,get_object_or_404
from .models import  LignePanier, Produit,Commande,Panier
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required



# Create your views here.
def home(request,*args,**kwargs):
    """Renders the home page."""
    return render(request,'home.html')

@login_required
def mon_compte(request):
    # Logique pour afficher les informations de l'utilisateur
    return render(request, 'mon_compte.html')

# pour afficher la liste des produits
def liste_produit (request):
    produits = Produit.objects.filter(disponible=True) # Récupère tous les produits de la base de données
    return render(request, 'liste_produit.html', {'produits': produits})  # Rend la page HTML avec les produits

# pour afficher les détails d'un produit spécifique
def detail_produit(request, pk):
    produit = Produit.objects.get(pk=pk)  # Récupère le produit correspondant à la clé primaire (pk)
    return render(request, 'detail_produit.html', {'produit': produit})  # Rend la page HTML avec les détails du produit

def ajouter_au_panier(request, produit_id):
    produit = get_object_or_404(Produit, id=produit_id)
    utilisateur = request.user

    # Essayer de récupérer un panier existant pour l'utilisateur
    panier, created = Panier.objects.get_or_create(utilisateur=utilisateur)

    # Ajouter le produit au panier
    if created:
        panier.save()  # Sauvegarder le panier seulement s'il a été créé

    # Code pour ajouter le produit au panier (par exemple, LignePanier)
    ligne_panier, created = LignePanier.objects.get_or_create(
        panier=panier,
        produit=produit,
        defaults={'quantite': 1}
    )

    if not created:
        ligne_panier.quantite += 1
        ligne_panier.save()

    return redirect('panier')



def panier(request):
    try:
        panier = Panier.objects.get(utilisateur=request.user)
    except Panier.DoesNotExist:
        panier = None
    # autre logique...
    return render(request, 'panier.html', {'panier': panier})
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
    return render(request, 'inscription.html', {'form': form})  # Rend la page d'inscription

# pour afficher la liste des commandes
def liste_commande (request):
    commandes = Commande.objects.all() # Récupère tous les commandes de la base de données
    return render(request, 'liste_commande.html', {'commandes': commandes})  # Rend la page HTML avec les commandes