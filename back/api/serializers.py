from rest_framework import serializers
from .models import NflUser, Equipe, Commentaire, Favoris

class NflUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NflUser
        fields = '__all__'

class EquipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipe
        fields = '__all__'

class CommentaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commentaire
        fields = '__all__'

class FavorisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favoris
        fields = '__all__'
