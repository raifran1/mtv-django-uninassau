from django.db import models


# veiculos #
class Veiculos(models.Model):
    concessionaria = models.ForeignKey('core.Concessionaria', on_delete=models.CASCADE, null=True)
    nome = models.CharField(max_length=50)
    cor = models.CharField(max_length=20)
    funciona = models.BooleanField()

    class Meta:
        verbose_name_plural = 'Veículos'

    def __str__(self):
        return self.nome


class Concessionaria(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField()
    numero_de_carros = models.PositiveIntegerField()
    funcionando = models.BooleanField()

    class Meta:
        verbose_name_plural = 'Concesionarias'

    def __str__(self):
        return self.nome

