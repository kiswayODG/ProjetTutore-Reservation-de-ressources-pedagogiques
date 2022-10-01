from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Personnel(models.Model):

    codePerso = models.fields.CharField(max_length=4)
    nom = models.fields.CharField(max_length=50)
    prenom = models.fields.CharField(max_length=50)
    sexe = models.fields.CharField
    typePerso = models.fields.CharField(max_length=1000)
    dateNaiss = models.fields.IntegerField(
    validators=[MinValueValidator(1900), MaxValueValidator(2004)])
    def __str__(self):
        return f'{self.nom}'


class Ressource(models.model):
    codeRess = models.fields.CharField(max_length = 5)
    typeRess = models.fields.CharField(max_lenth = 100)
    def __str__(self):
        return f'{self.typeRess}'