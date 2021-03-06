from django.db import models

class Pergunta(models.Model):
    numero = models.IntegerField(verbose_name="Número", null=False, blank=False, unique=True)
    texto = models.TextField(verbose_name="Pergunta", null=False, blank=False)

    created_at = models.DateTimeField(' Criado em ', auto_now_add=True)         # Grava data de criação
    updated_at = models.DateTimeField(' Atualizado em ', auto_now=True)          # Grava data de atualização

    def __str__(self):
        return self.texto

    class Meta:
        verbose_name = 'Pergunta'
        verbose_name_plural = 'Perguntas'
