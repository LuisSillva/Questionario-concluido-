from django.db import models

# Create your models here.

class Resposta(models.Model):
    pergunta = models.CharField(max_length=255)
    resposta_texto = models.TextField(null=True, blank=True)
    resposta_numero = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.pergunta