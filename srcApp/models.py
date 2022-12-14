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

class Role(models.Model):
    code= models.fields.CharField(max_length=4)
    role=  models.fields.CharField(max_length=50)

    def __str__(self):
        return f'{self.role}'

class Personnel(models.Model):
    codePerso = models.fields.CharField(max_length=4)
    nom = models.fields.CharField(max_length=50)
    prenom = models.fields.CharField(max_length=50)
    typePerso = models.ForeignKey(TypePerso, null=True, on_delete=models.SET_NULL)
    dateNaiss = models.fields.IntegerField(
    validators=[MinValueValidator(1900), MaxValueValidator(2004)])
    chefService = models.BooleanField
    compte = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    #username = models.fields.CharField(max_length=50)
    #motDepass = models.fields.CharField(validators=[MinLengthValidator(8, message='Veuillez taper un mot de passe à 8 caractère min')], max_length=50,null=False)

    def __str__(self):
        return f'{self.nom}'

class TypeRess(models.Model):
    codeType = models.fields.CharField(max_length=4)
    ress = models.fields.CharField(max_length=50)

    def __str__(self):
        return f'{self.ress}'
class Ressource(models.Model):
    typeRess = models.ForeignKey(TypeRess, null=True, on_delete=models.SET_NULL)
    codeRess = models.fields.CharField(max_length = 5)
    nomRess = models.fields.CharField(max_length=50)
    def __str__(self):
        return f'{self.nomRess}'

class Reservation(models.Model):
    reservateur = models.ForeignKey(Personnel, on_delete=models.CASCADE)
    ressource = models.ForeignKey(Ressource, on_delete=models.CASCADE)
    date_de_reservation = models.DateField()
    motif_de_reservation = models.CharField(max_length=255)
    UniqueConstraint(fields=['ressource', 'date_de_reservation'], name='reservation_unique_de_la_ressource_par_date')
