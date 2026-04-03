from rest_framework import viewsets
from .models import f1User, Equipe,Circuit, Commentaire, Favoris, Prefere
from .serializers import (
    f1UserSerializer, EquipeSerializer,CircuitSerializer,
    CommentaireSerializer, FavorisSerializer, PrefereSerializer
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
import uuid


class f1UserViewSet(viewsets.ModelViewSet):
    queryset = f1User.objects.all()
    serializer_class = f1UserSerializer

class EquipeViewSet(viewsets.ModelViewSet):
    queryset = Equipe.objects.all()
    serializer_class = EquipeSerializer

class CircuitViewSet(viewsets.ModelViewSet):
    queryset = Circuit.objects.all()
    serializer_class = CircuitSerializer

class CommentaireViewSet(viewsets.ModelViewSet):
    queryset = Commentaire.objects.all()
    serializer_class = CommentaireSerializer

class FavorisViewSet(viewsets.ModelViewSet):
    queryset = Favoris.objects.all()
    serializer_class = FavorisSerializer

class PrefereViewSet(viewsets.ModelViewSet):
    queryset = Prefere.objects.all()
    serializer_class = PrefereSerializer

class LoginView(APIView):
    def post(self, request):
        login = request.data.get("login")
        mdp = request.data.get("mdp")

        if not login or not mdp:
            return Response({"error": "Champs manquants"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = f1User.objects.get(login=login)
        except f1User.DoesNotExist:
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

        if f1User.objects.filter(login=login).exists():
            return Response({"error": "Login déjà utilisé"}, status=status.HTTP_400_BAD_REQUEST)

        id_user = str(uuid.uuid4())

        user = f1User.objects.create(
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
