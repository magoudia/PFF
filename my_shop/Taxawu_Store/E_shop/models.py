from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Modèle représentant une catégorie de produits
class Categorie(models.Model):
    # Nom de la catégorie
    nom = models.CharField(max_length=255)
    # Description optionnelle de la catégorie
    description = models.TextField(blank=True, null=True)


# Modèle représentant un produit dans la boutique
class Produit(models.Model):
    # Nom du produit
    nom = models.CharField(max_length=255)
    # Description détaillée du produit
    description = models.TextField()
    # Prix du produit
    prix = models.DecimalField(max_digits=10, decimal_places=2) # la fonction max_digits gère le nombre tota de chifrres et 
    #la fonction decimal_places gère le nombre de chiffre après la virgule.

    # Image associée au produit (facultative)
    image = models.ImageField(upload_to='produits/', blank=True, null=True) # le champ immage est optionnel
    #la fonction upload_to est utilisé pour stocker les images de produits dans un répertoire

    # Quantité en stock
    stock = models.IntegerField()
    # Catégorie du produit (relation avec le modèle Categorie)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    # Date à laquelle le produit a été ajouté
    date_ajout = models.DateTimeField(auto_now_add=True) # le auto_now_add=True montre que le champ ser automatiquement rempli 



# Modèle représentant un panier d'achat pour un utilisateur
class Panier(models.Model):
    # Utilisateur propriétaire du panier (relation avec le modèle User)
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    # Date de création du panier
    date_creation = models.DateTimeField(auto_now_add=True) # le auto_now_add=True montre que le champ ser automatiquement rempli

# Modèle représentant un élément dans un panier d'achat
class ElementPanier(models.Model):
    # Panier auquel appartient cet élément
    panier = models.ForeignKey(Panier, on_delete=models.CASCADE)
    # Produit ajouté au panier
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    # Quantité de ce produit dans le panier
    quantite = models.IntegerField()

# Modèle représentant une commande passée par un utilisateur
class Commande(models.Model):
    # Choix de statut pour la commande
    STATUT_CHOIX = [
        ('en_attente', 'En attente'),
        ('expediee', 'Expédiée'),
        ('livree', 'Livrée'),
        ('annulee', 'Annulée'),
    ]
    # Utilisateur ayant passé la commande
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    # Montant total de la commande
    total = models.DecimalField(max_digits=10, decimal_places=2)
    # Statut actuel de la commande
    statut = models.CharField(max_length=10, choices=STATUT_CHOIX, default='en_attente')
    # Date à laquelle la commande a été passée
    date_commande = models.DateTimeField(auto_now_add=True)

# Modèle représentant un élément d'une commande
class ElementCommande(models.Model):
    # Commande à laquelle cet élément est associé
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    # Produit commandé
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    # Quantité de ce produit dans la commande
    quantite = models.IntegerField()
    # Prix unitaire du produit au moment de la commande
    prix = models.DecimalField(max_digits=10, decimal_places=2)

# Modèle représentant un paiement effectué pour une commande
class Paiement(models.Model):
    # Choix de méthodes de paiement
    METHODE_CHOIX = [
        ('carte_credit', 'Carte de crédit'),
        ('paypal', 'PayPal'),
        ('virement_bancaire', 'Virement bancaire'),
    ]
    # Commande pour laquelle ce paiement a été effectué
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    # Montant du paiement
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    # Méthode de paiement utilisée
    methode = models.CharField(max_length=20, choices=METHODE_CHOIX)
    # Statut du paiement (en attente, réussi, etc.)
    statut = models.CharField(max_length=10, default='en_attente')
    # Date à laquelle le paiement a été effectué
    date_paiement = models.DateTimeField(auto_now_add=True)

# Modèle représentant un avis et une notation pour un produit
class Avis(models.Model):
    # Utilisateur ayant laissé l'avis
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    # Produit sur lequel porte l'avis
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    # Note donnée par l'utilisateur (généralement sur 5)
    note = models.IntegerField()
    # Commentaire optionnel de l'utilisateur
    commentaire = models.TextField(blank=True, null=True)
    # Date de création de l'avis
    date_creation = models.DateTimeField(auto_now_add=True)

# Modèle représentant les informations de livraison pour une commande
class Livraison(models.Model):
    # Commande pour laquelle cette livraison est effectuée
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    # Adresse de livraison
    adresse = models.CharField(max_length=255)
    # Nom du transporteur
    transporteur = models.CharField(max_length=255)
    # Numéro de suivi fourni par le transporteur
    numero_suivi = models.CharField(max_length=255)
    # Date à laquelle la commande a été expédiée
    date_expedition = models.DateTimeField(auto_now_add=True)
    # Date prévue de livraison
    date_livraison = models.DateTimeField()

# Modèle représentant une requête de recherche effectuée par un utilisateur
class Recherche(models.Model):
    # Utilisateur ayant effectué la recherche (facultatif)
    utilisateur = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    # Texte de la requête de recherche
    requete = models.CharField(max_length=255)
    # Date à laquelle la recherche a été effectuée
    date_recherche = models.DateTimeField(auto_now_add=True)