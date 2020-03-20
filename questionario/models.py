from django.db import models

class Questionario(models.Model):
    numero = models.IntegerField(verbose_name="Número", null=False, blank=False, unique=True)
    tipo = models.CharField(max_length=30, verbose_name="Tipo", null=False, blank=False)

    created_at = models.DateTimeField(' Criado em ', auto_now_add=True)         # Grava data de criação
    updated_at = models.DateTimeField(' Atualizado em ', auto_now=True)          # Grava data de atualização

    def __str__(self):
        return self.tipo

    class Meta:
        verbose_name = 'Questionário'
        verbose_name_plural = 'Questionários'
