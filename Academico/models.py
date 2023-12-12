from itertools import chain
from pickle import TRUE
from django.db import models

# Create your models here.
class Curso(models.Model):
    #codigo = models.CharField(max_length=6)
    nombre = models.CharField(max_length = 50)
    #encargado = models.CharField(max_length = 5)
    creditos = models.PositiveBigIntegerField()
    
