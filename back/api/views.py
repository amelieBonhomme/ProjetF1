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
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.db.models import Count

from django.views.decorators.csrf import csrf_exempt
import json
from datetime import date
from django.shortcuts import get_object_or_404


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

# ------------------------------------------   gestion login ---------------------------------------------------
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
    
# ----------------------------------------------------------   Gestion des favoris ----------------------------------

@api_view(['GET'])
def get_favoris_user(request, id_user):
    favoris = Favoris.objects.filter(user_id=id_user)
    equipes_ids = favoris.values_list("equipe_id", flat=True)
    return Response(list(equipes_ids))


@api_view(['POST'])
def toggle_favori(request):
    # on récupère les infos de l'action
    user_id = request.data.get("user_id")
    equipe_id = request.data.get("equipe_id")

    # on vérifie qu'on a les infos
    if not user_id or not equipe_id:
        return Response({"error": "Champs manquants"}, status=400)
    
    # on vérifie que l'user et l'équipe existe
    user = get_object_or_404(f1User, id_user=user_id)
    equipe = get_object_or_404(Equipe, id_equipe=equipe_id)

    # On supprime ou ajoute l'utilisateur
    try:
        favori = Favoris.objects.get(user=user, equipe=equipe)
        favori.delete()
        return Response({"status": "removed"})
    except Favoris.DoesNotExist:
        Favoris.objects.create(user=user, equipe=equipe)
        return Response({"status": "added"})
    
# ----------------------------------------------------------   Gestion des circuits ----------------------------------

@api_view(['GET'])
def get_prefere_user(request, id_user):
    prefere = Prefere.objects.filter(user_id=id_user)
    circuit_ids = prefere.values_list("circuit_id", flat=True)
    return Response(list(circuit_ids))


@api_view(['POST'])
def toggle_prefere(request):
    # on récupère les infos
    user_id = request.data.get("user_id")
    circuit_id = request.data.get("circuit_id")

    if not user_id or not circuit_id:
        return Response({"error": "Champs manquants"}, status=400)
    
    # on vérifie que l'user et l'équipe existe
    user = get_object_or_404(f1User, id_user=user_id)
    circuit = get_object_or_404(Circuit, id_circuit=circuit_id)

    try:
        # On supprime les valeurs vérifier
        prefere = Prefere.objects.get(user = user, circuit = circuit)
        prefere.delete()
        return Response({"status": "removed"})
    # Si sa n'existe pas on rentre dans l'exemption
    except Prefere.DoesNotExist:
        # On ajoute les valeurs vérifier
        Prefere.objects.create(user = user, circuit = circuit)
        return Response({"status": "added"})

# ----------------------------------------------------------   Satistiques ----------------------------------

def stats_sexe(request):
    data = f1User.objects.values('sexe').annotate(total=Count('sexe'))
    result = {item['sexe']: item['total'] for item in data}
    return JsonResponse(result)

# ----------------------------------------------------------   commentaire  ----------------------------------

def get_commentaires(request):
    commentaires = Commentaire.objects.select_related("user").order_by("-date")[:10]
    data = [
        {
            "id": c.id_commentaire,
            "texte": c.texte,
            "date": c.date,
            "user": {
                "id": c.user.id_user,
                "login": c.user.login
            }
        }
        for c in commentaires
    ]
    return JsonResponse(data, safe=False)

@api_view(['POST'])
def add_commentaire(request):
    # on évite les méthode get
    if request.method != "POST":
        return JsonResponse({"error": "Méthode non autorisée"}, status=405)

    # On extrait les infos
    texte = request.data.get("texte")
    id_user = request.data.get("id_user")

    # On vérifie que ce n'est pas vide
    if not texte or not id_user:
        return JsonResponse({"error": "Champs manquants"}, status=400)
    
    user = f1User.objects.filter(id_user=id_user).first()
    if not user:
        return JsonResponse({"error":"Utilisateur introuvable"}, status=404)

    new_comment = Commentaire.objects.create(
        id_commentaire=str(uuid.uuid4()),
        texte=texte,
        date=date.today(),
        user=user
    )

    return JsonResponse({"success": True})

