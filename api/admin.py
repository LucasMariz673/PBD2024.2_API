from django.contrib import admin

from api.models import Empreendimeto, Imagen

# Register your models here.

class ImagenInLine(admin.TabularInline):
    model = Imagen

class EmpreendimentoAdmin(admin.ModelAdmin):
    inlines = [ImagenInLine]

admin.site.register(Empreendimeto, EmpreendimentoAdmin)
admin.site.register(Imagen)