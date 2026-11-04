from django.db import models
from django.contrib.auth.models import AbstractUser
class Utilisateur(AbstractUser):

    class Role(models.TextChoices):
        ADMIN = 'ADMIN', 'Administrateur'
        UTILISATEUR = 'UTILISATEUR', 'Utilisateur'

    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.UTILISATEUR
    )

    date_creation = models.DateTimeField(auto_now_add=True)