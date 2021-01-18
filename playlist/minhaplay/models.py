from django.db import models

# Create your models here.

class Faixa(models.Model):
    nome = models.CharField(max_length=100)
    artista = models.CharField(max_length=100)
    url = models.URLField(max_length=100)
    letra = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Faixas'

    def __str__(self):
        return self.nome