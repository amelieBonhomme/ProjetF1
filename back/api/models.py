from django.db import models

class NflUser(models.Model):
    id_user = models.CharField(primary_key=True, max_length=50)
    nom = models.CharField(max_length=50, blank=True, null=True)
    prenom = models.CharField(max_length=50, blank=True, null=True)
    sexe = models.CharField(max_length=50, blank=True, null=True)
    mail = models.CharField(max_length=50, blank=True, null=True)
    date_naissance = models.DateField(blank=True, null=True)
    mdp = models.CharField(max_length=50, blank=False, null=False)
    login = models.CharField(max_length=50, blank=False, null=False)

    class Meta:
        db_table = 'nfl_user'


class Equipe(models.Model):
    id_equipe = models.CharField(primary_key=True, max_length=50)
    nom = models.CharField(max_length=50, blank=True, null=True)
    logo = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'equipe'  


class Commentaire(models.Model):
    id_commentaire = models.CharField(primary_key=True, max_length=50)
    texte = models.TextField(blank=True, null=True)
    user = models.ForeignKey('NflUser', on_delete=models.CASCADE, db_column='id_user')

    class Meta:
        db_table = 'commentaire'


class Favoris(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('NflUser', on_delete=models.CASCADE, db_column='id_user')
    equipe = models.ForeignKey('Equipe', on_delete=models.CASCADE, db_column='id_equipe')

    class Meta:
        db_table = 'favoris'
        unique_together = (('user', 'equipe'),)
