#pour les variables de env
import os
#apple de bib django 
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LifePilotAI.settings')
#pert de travail avec l'utilisation de para de projet 
django.setup()
#bib pour connection de  django avec bd
from django.db import connection

try:
    #ouverture de connection avec bd
    connection.ensure_connection()
    print("SUCCESS: Django est connectée à PostgreSQL")
except Exception as e:
    print("ECHEC: Connexion impossible")
    print("Erreur:", e)