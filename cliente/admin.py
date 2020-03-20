from django.contrib import admin
from cliente.models import Cliente

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cpf', 'dtNascimento']  # Campos que aparecem na listagem dos objetos no admin
    search_fields = ['nome', 'cpf ']  # Campos pesquisáveis no admin
    list_filter = ['nome', 'cpf']
    #list_editable = ['nome', 'meta']

admin.site.register(Cliente, ClienteAdmin)