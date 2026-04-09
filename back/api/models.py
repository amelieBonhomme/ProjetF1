from django.db import models

class f1User(models.Model):
    id_user = models.CharField(primary_key=True, max_length=50)
    nom = models.CharField(max_length=50, blank=True, null=True)
    prenom = models.CharField(max_length=50, blank=True, null=True)
    sexe = models.CharField(max_length=50, blank=True, null=True)
    mail = models.CharField(max_length=50, blank=True, null=True)
    date_naissance = models.DateField(blank=True, null=True)
    mdp = models.CharField(max_length=50, blank=False, null=False)
    login = models.CharField(max_length=50, blank=False, null=False)

    class Meta:
        db_table = 'f1_user'


class Equipe(models.Model):
    id_equipe = models.CharField(primary_key=True, max_length=50)
    nom = models.CharField(max_length=50, blank=True, null=True)
    logo = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    pilote_principal = models.TextField(blank=True, null=True)
    image_pilote = models.TextField(blank=True, null=True)
    pilote_second = models.TextField(blank=True, null=True)
    image_pilote2 = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'equipe'  

class Circuit(models.Model):
    id_circuit = models.CharField(primary_key=True, max_length=50)
    nom_circuit = models.CharField(max_length=50, blank=True, null=True)
    image_circuit = models.TextField(blank=True, null=True)
    description_circuit = models.TextField(blank=True, null=True)
    lien_site = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'circuit'  



class Commentaire(models.Model):
    id_commentaire = models.CharField(primary_key=True, max_length=50)
    texte = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    user = models.ForeignKey('f1User', on_delete=models.CASCADE, db_column='id_user')

    class Meta:
        db_table = 'commentaire'


class Favoris(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('f1User', on_delete=models.CASCADE, db_column='id_user')
    equipe = models.ForeignKey('Equipe', on_delete=models.CASCADE, db_column='id_equipe')

    class Meta:
        db_table = 'favoris'
        unique_together = (('user', 'equipe'),)

class Prefere(models.Model):
    id = models.AutoField(primary_key=True)  # ⭐ NOUVEAU CHAMP ID
    user = models.ForeignKey('f1User', on_delete=models.CASCADE, db_column='id_user')
    circuit = models.ForeignKey('Circuit', on_delete=models.CASCADE, db_column='id_circuit')

    class Meta:
        db_table = 'prefere'
        unique_together = (('user', 'circuit'),)
        managed = False



