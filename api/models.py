from django.db import models

# Create your models here.

class Empreendimeto(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    total_lotes = models.IntegerField()
    total_disponivel = models.IntegerField()

    objects = models.Manager()

    def __str__(self):
        return  self.nome

class Imagen(models.Model):
    imagen = models.ImageField()
    empreendimento = models.ForeignKey(Empreendimeto, on_delete=models.CASCADE)

    def __str__(self):
        return  self.imagen.name