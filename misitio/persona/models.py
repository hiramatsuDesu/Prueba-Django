from django.db import models

# Create your models here.


class Persona(models.Model):
    nombre = models.CharField(max_length=50, blank=False)
    apellido = models.CharField(max_length=50, blank=False)
    mail = models.EmailField(("Mail"), max_length=254)
