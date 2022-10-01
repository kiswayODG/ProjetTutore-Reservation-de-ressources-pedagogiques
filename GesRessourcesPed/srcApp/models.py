from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class TypePerso(models.Model):
    codeType = models.fields.CharField(max_length=4)
    fonction = models.fields.CharField(max_length=50)
    chefService = models.BooleanField


class Personnel(models.Model):

    codePerso = models.fields.CharField(max_length=4)
    nom = models.fields.CharField(max_length=50)
    prenom = models.fields.CharField(max_length=50)
    sexe = models.fields.CharField
    typePerso = models.ForeignKey(TypePerso, null=True, on_delete=models.SET_NULL)
    dateNaiss = models.fields.IntegerField(
    validators=[MinValueValidator(1900), MaxValueValidator(2004)])

    def __str__(self):
        return f'{self.nom}'


class Ressource(models.Model):
    natureRes = models.TextChoices ('Batiment','Matériel')

    codeRess = models.fields.CharField(max_length = 5)
    typeRess = models.fields.CharField(choices=natureRes.choices, max_length=10)
    nomRess = models.fields.CharField(max_length=50)
    def __str__(self):
        return f'{self.nomRess}'