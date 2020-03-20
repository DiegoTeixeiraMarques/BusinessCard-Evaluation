from django.contrib import admin
from .models import Empresa

class EmpresaAdmin(admin.ModelAdmin):
    fields = ['nome', 'cnpj']
    list_display = ['nome', 'cnpj']  # Campos que aparecem na listagem dos objetos no admin
    search_fields = ['nome', 'segmento']  # Campos pesquisáveis no admin
    #list_filter = ['nome', 'cnpj', 'segmento']
    #list_editable = ['nome', 'meta']

admin.site.register(Empresa, EmpresaAdmin)