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

    def validate_texte(self, value):
        if not value.strip():
            raise serializers.ValidationError("Le commentaire ne peut pas être vide.")
        if len(value) > 500:
            raise serializers.ValidationError("Le commentaire est trop long (500 caractères max).")
        return value

    def validate(self, data):
        # Vérifier que l'utilisateur existe
        if not f1User.objects.filter(id_user=data["id_user"]).exists():
            raise serializers.ValidationError("Utilisateur inexistant.")

        return data

class FavorisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favoris
        fields = '__all__'

    def validate(self, data):
        # Vérifier que l'utilisateur existe
        if not f1User.objects.filter(id_user=data["id_user"]).exists():
            raise serializers.ValidationError("Utilisateur inexistant.")

        # Vérifier que l'équipe existe
        if not Equipe.objects.filter(id_equipe=data["id_equipe"]).exists():
            raise serializers.ValidationError("Équipe inexistante.")

        # Empêcher les doublons
        if Favoris.objects.filter(id_user=data["id_user"], id_equipe=data["id_equipe"]).exists():
            raise serializers.ValidationError("Cette équipe est déjà dans les favoris.")

        return data


class PrefereSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prefere
        fields = '__all__'

    def validate(self, data):
        if not f1User.objects.filter(id_user=data["id_user"]).exists():
            raise serializers.ValidationError("Utilisateur inexistant.")

        if not Circuit.objects.filter(id_circuit=data["id_circuit"]).exists():
            raise serializers.ValidationError("Circuit inexistant.")

        if Prefere.objects.filter(id_user=data["id_user"], id_circuit=data["id_circuit"]).exists():
            raise serializers.ValidationError("Ce circuit est déjà dans les préférés.")

        return data
