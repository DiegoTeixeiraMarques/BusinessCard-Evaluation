from django.db import models
from cliente.models import Cliente
from funcionario.models import Funcionario
from questionario.models import Questionario

class Atendimento(models.Model):
    numero = models.BigIntegerField(verbose_name="Atendimento", unique=True, blank=False, null=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='cliente', verbose_name="Cliente", null=True, blank=True)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE, related_name='funcionario', verbose_name="Funcionário", null=True, blank=True)
    questionario = models.ForeignKey(Questionario, on_delete=models.CASCADE, related_name='questionario', verbose_name="Questionário", null=True, blank=True)
    dtAtendimento = models.DateTimeField(verbose_name="Data/Hora", null=False, blank=False)

    def __str__(self):
        return str(self.numero) + '/ ' + str(self.funcionario) + '/ ' + str(self.cliente) + '/ ' + str(self.dtAtendimento.date()) +     '/ ' + str(self.dtAtendimento.time())

    class Meta:
        verbose_name = 'Atendimento'
        verbose_name_plural = 'Atendimentos'