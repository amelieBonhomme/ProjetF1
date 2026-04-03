from rest_framework import serializers
from .models import f1User, Equipe,Circuit, Commentaire, Favoris, Prefere

class f1UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = f1User
        fields = '__all__'

class EquipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipe
        fields = '__all__'

class CircuitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Circuit
        fields = '__all__'

class CommentaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commentaire
        fields = '__all__'

class FavorisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favoris
        fields = '__all__'

class PrefereSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prefere
        fields = '__all__'