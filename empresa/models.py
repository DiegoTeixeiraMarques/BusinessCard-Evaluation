from django.db import models

class Empresa(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome", blank=False, null=False)
    cnpj = models.CharField(max_length=14, verbose_name="CNPJ", unique=True, blank=False, null=False)
    segmento = [(
        'Vestuário',
        'Alimentação'
    )]

    created_at = models.DateTimeField(' Criado em ', auto_now_add=True)  # Grava data de criação
    updated_at = models.DateTimeField(' Atualizado em ', auto_now=True)  # Grava data de atualização

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"
