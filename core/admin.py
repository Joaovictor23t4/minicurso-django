from django.contrib import admin

from .models import Categoria, TipoAtuacao, Pais, Produtora, Membro, Filme, Atuacao

class AtuacaoInline(admin.TabularInline):
    model = Atuacao

admin.site.register(Categoria)
admin.site.register(TipoAtuacao)
admin.site.register(Pais)
admin.site.register(Produtora)
# admin.site.register(Membro)
# admin.site.register(Filme)

@admin.register(Membro)
class MembroAdmin(admin.ModelAdmin):
    model = Atuacao

@admin.register(Filme)
class FilmeAdmin(admin.ModelAdmin):
    inlines = [AtuacaoInline]

# python manage.py makemigrations
# python manage.py migrate
# python manage.py runserver
