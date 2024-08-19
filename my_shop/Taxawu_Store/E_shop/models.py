from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Modèle représentant une catégorie de produits
class Categorie(models.Model):
    # Nom de la catégorie
    nom = models.CharField(max_length=255)
    # Description optionnelle de la catégorie
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nom  # Affiche le nom de la catégorie dans l'administration


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
    image = models.ImageField(upload_to='produits/') # le champ immage est optionnel
    #la fonction upload_to est utilisé pour stocker les images de produits dans un répertoire

    # Quantité en stock
    stock = models.IntegerField()
    # Catégorie du produit (relation avec le modèle Categorie)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    # Date à laquelle le produit a été ajouté
    date_ajout = models.DateTimeField(auto_now_add=True) # le auto_now_add=True montre que le champ ser automatiquement rempli 


    def __str__(self):
        return self.nom  # Affiche le nom du produit dans l'administration




# Modèle représentant un panier d'achat pour un utilisateur
class Panier(models.Model):
    # Utilisateur propriétaire du panier (relation avec le modèle User)
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    # Date de création du panier
    date_creation = models.DateTimeField(auto_now_add=True) # le auto_now_add=True montre que le champ ser automatiquement rempli

    def __str__(self):
        return f"Panier de {self.utilisateur}"  # Affiche le propriétaire du panier




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

    def __str__(self):
        return f"Commande de {self.utilisateur} le {self.date_commande}"  # Affiche un résumé de la commande