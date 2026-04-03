from rest_framework import serializers
from .models import f1User, Equipe, Commentaire, Favoris

class f1UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = f1User
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
