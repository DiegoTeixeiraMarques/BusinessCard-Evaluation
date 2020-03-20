from django.contrib import admin
from questionario.models import Questionario

class QuestionarioAdmin(admin.ModelAdmin):
    list_display = ['numero', 'tipo']  # Campos que aparecem na listagem dos objetos no admin
    search_fields = ['numero', 'tipo ']  # Campos pesquisáveis no admin
    list_filter = ['numero', 'tipo']
    #list_editable = ['nome', 'meta']

admin.site.register(Questionario, QuestionarioAdmin)
