from rest_framework import viewsets
from .models import NflUser, Equipe, Commentaire, Favoris
from .serializers import (
    NflUserSerializer, EquipeSerializer,
    CommentaireSerializer, FavorisSerializer
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
import uuid


class NflUserViewSet(viewsets.ModelViewSet):
    queryset = NflUser.objects.all()
    serializer_class = NflUserSerializer

class EquipeViewSet(viewsets.ModelViewSet):
    queryset = Equipe.objects.all()
    serializer_class = EquipeSerializer

class CommentaireViewSet(viewsets.ModelViewSet):
    queryset = Commentaire.objects.all()
    serializer_class = CommentaireSerializer

class FavorisViewSet(viewsets.ModelViewSet):
    queryset = Favoris.objects.all()
    serializer_class = FavorisSerializer

class LoginView(APIView):
    def post(self, request):
        login = request.data.get("login")
        mdp = request.data.get("mdp")

        if not login or not mdp:
            return Response({"error": "Champs manquants"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = NflUser.objects.get(login=login)
        except NflUser.DoesNotExist:
            return Response({"error": "Utilisateur introuvable"}, status=status.HTTP_404_NOT_FOUND)

        if not check_password(mdp, user.mdp):
            return Response({"error": "Mot de passe incorrect"}, status=status.HTTP_401_UNAUTHORIZED)

        return Response({
            "message": "Connexion réussie",
            "id_user": user.id_user,
            "nom": user.nom,
            "prenom": user.prenom,
            "mail": user.mail
        })

class RegisterView(APIView):
    def post(self, request):
        login = request.data.get("login")
        mdp = request.data.get("mdp")
        nom = request.data.get("nom")
        prenom = request.data.get("prenom")
        sexe = request.data.get("sexe")
        date_naissance = request.data.get("date_naissance")
        mail = request.data.get("mail")

        if not login or not mdp or not nom or not prenom or not mail or not sexe or not date_naissance:
            return Response({"error": "Champs manquants"}, status=status.HTTP_400_BAD_REQUEST)

        if NflUser.objects.filter(login=login).exists():
            return Response({"error": "Login déjà utilisé"}, status=status.HTTP_400_BAD_REQUEST)

        id_user = str(uuid.uuid4())

        user = NflUser.objects.create(
            id_user=id_user,
            login=login,
            mdp=make_password(mdp),
            nom=nom,
            prenom=prenom,
            sexe=sexe,
            date_naissance=date_naissance,
            mail=mail
        )

        return Response({
            "message": "Inscription réussie",
            "id_user": user.id_user,
            "nom": user.nom,
            "prenom": user.prenom,
            "mail": user.mail
        }, status=status.HTTP_201_CREATED)
