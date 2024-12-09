from django.db import models

# Create your models here.

class Empreendimento(models.Model):
    id = models.AutoField
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    total_lotes = models.IntegerField(editable=False, default=0)
    total_disponivel = models.IntegerField(editable=False, default=0)

    objects = models.Manager()

    def __str__(self):
        return  self.nome

class Imagem(models.Model):
    id = models.AutoField
    empreendimento = models.ForeignKey(Empreendimento, on_delete=models.CASCADE, related_name='imagens')
    imagem = models.ImageField()

    objects = models.Manager()

    def __str__(self):
        return  self.imagem.name