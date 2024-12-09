from django.contrib import admin

from api.models import Empreendimento, Imagem

# Register your models here.

class ImagenInLine(admin.TabularInline):
    model = Imagem

class EmpreendimentoAdmin(admin.ModelAdmin):
    inlines = [ImagenInLine]

admin.site.register(Empreendimento, EmpreendimentoAdmin)
admin.site.register(Imagem)