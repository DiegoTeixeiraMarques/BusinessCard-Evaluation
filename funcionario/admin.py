from django.contrib import admin
from .models import Funcionario

class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cpf', 'empresa']  # Campos que aparecem na listagem dos objetos no admin
    search_fields = ['nome', 'cpf', 'empresa']  # Campos pesquisáveis no admin
    list_filter = ['empresa', 'nome']
    #list_editable = ['nome', 'meta']

admin.site.register(Funcionario, FuncionarioAdmin)