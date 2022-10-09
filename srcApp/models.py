from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator,MinLengthValidator
from django.db.models import UniqueConstraint
from django.contrib.auth.models import User

# Create your models here.
class TypePerso(models.Model):
    codeType = models.fields.CharField(max_length=4)
    fonction = models.fields.CharField(max_length=50)

    def __str__(self):
        return f'{self.fonction}'



class Personnel(models.Model):
    rolelist = models.TextChoices('Utilisateur', 'Administrateur')
    codePerso = models.fields.CharField(max_length=4)
    nom = models.fields.CharField(max_length=50)
    prenom = models.fields.CharField(max_length=50)
    typePerso = models.ForeignKey(TypePerso, null=True, on_delete=models.SET_NULL)
    dateNaiss = models.fields.IntegerField(
    validators=[MinValueValidator(1900), MaxValueValidator(2004)])
    chefService = models.BooleanField
    role = models.fields.CharField(choices=rolelist.choices, max_length=50)
    account = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    #username = models.fields.CharField(max_length=50)
    #motDepass = models.fields.CharField(validators=[MinLengthValidator(8, message='Veuillez taper un mot de passe à 8 caractère min')], max_length=50,null=False)

    def __str__(self):
        return f'{self.nom}'


class Ressource(models.Model):
    natureRes = models.TextChoices ('Batiment','Matériel')

    codeRess = models.fields.CharField(max_length = 5)
    typeRess = models.fields.CharField(choices=natureRes.choices, max_length=10)
    nomRess = models.fields.CharField(max_length=50)

    def __str__(self):
        return f'{self.nomRess}'

class Reservation(models.Model):
    reservateur = models.ForeignKey(Personnel, on_delete=models.CASCADE)
    ressource = models.ForeignKey(Ressource, on_delete=models.CASCADE)
    date_de_reservation = models.DateField()
    motif_de_reservation = models.CharField(max_length=255)
    UniqueConstraint(fields=['ressource', 'date_de_reservation'], name='reservation_unique_de_la_ressource_par_date')

