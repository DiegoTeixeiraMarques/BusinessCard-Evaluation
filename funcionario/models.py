from django.db import models
from empresa.models import Empresa 

class Funcionario(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='empresa', verbose_name="Empresa", null=False, blank=False)
    nome = models.CharField(max_length=255, verbose_name="Nome", null=False, blank=False)
    cpf = models.CharField(max_length=11, verbose_name="CPF", help_text="Digite somente números", null=True, blank=True)
    qrcode = models.ImageField(verbose_name="QrCode", blank=True, null=True)
    dtNascimento = models.DateField(verbose_name="Data de nascimento", blank=True, null=True)

    created_at = models.DateTimeField(' Criado em ', auto_now_add=True)         # Grava data de criação
    updated_at = models.DateTimeField(' Atualizado em ', auto_now=True)          # Grava data de atualização

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'
