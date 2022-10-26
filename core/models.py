from django.db import models


# veiculos #
class Veiculos(models.Model):
    nome = models.CharField(max_length=50)
    cor = models.CharField(max_length=20)
    funciona = models.BooleanField()

    class Meta:
        verbose_name_plural = 'Veículos'

    def __str__(self):
        return self.nome