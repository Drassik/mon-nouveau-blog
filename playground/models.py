from django.db import models

# Create your models here.
from django.db import models
 
class Port(models.Model):
    id_port = models.CharField(max_length=100, primary_key=True)
    disponibilite = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='ports/', blank=True, null=True)
    def __str__(self):
        return self.id_port
 
 
class Bateau(models.Model):
    id_bateau = models.CharField(max_length=100, primary_key=True)
    etat = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    capacite = models.IntegerField()
    photo = models.ImageField(upload_to='bateaux/', blank=True, null=True)
    lieu = models.ForeignKey(Port, on_delete=models.CASCADE)
    def __str__(self):
        return self.id_bateau
