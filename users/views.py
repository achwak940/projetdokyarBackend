#utiliser pour retourne des templates html a l'utilisateur
from django.shortcuts import render
#admet des classes pert facilite la creation des apis
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from .serializers import InscriptionSerializer

class InscriptionView(generics.CreateAPIView):

    serializer_class = InscriptionSerializer