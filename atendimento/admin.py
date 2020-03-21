from django.contrib import admin
from .models import Atendimento

class AtendimentoAdmin(admin.ModelAdmin):
    list_display = ['numero', 'cliente', 'funcionario', 'dtAtendimento']  # Campos que aparecem na listagem dos objetos no admin
    search_fields = ['numero', 'cliente', 'funcionario']  # Campos pesquisáveis no admin
    list_filter = ['numero', 'cliente', 'funcionario']
    #list_editable = ['nome', 'meta']

admin.site.register(Atendimento, AtendimentoAdmin)
