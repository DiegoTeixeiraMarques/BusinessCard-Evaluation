from django.contrib import admin
from pergunta.models import Pergunta

class PerguntaAdmin(admin.ModelAdmin):
    list_display = ['numero', 'texto']  # Campos que aparecem na listagem dos objetos no admin
    search_fields = ['numero', 'texto ']  # Campos pesquisáveis no admin
    list_filter = ['numero', 'texto']
    #list_editable = ['nome', 'meta']

admin.site.register(Pergunta, PerguntaAdmin)