from django.db import models

# Create your models here.
class Soldado(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 100)
    arma = models.CharField(max_length = 50)
    arma_dps = models.IntegerField()
    arma_type = models.CharField(max_length = 50)


class History(models.Model):
    id = models.AutoField(primary_key = True)
    id_soldado = models.ForeignKey("Soldado", on_delete=models.CASCADE)
    arma = models.CharField(max_length = 50)