from django import forms
from .models import Empreendimento, Imagem

class EmpreendimentoForm(forms.ModelForm):
    class Meta:
        model = Empreendimento
        fields = ['nome', 'endereco']

class ImagemForm(forms.ModelForm):
    class Meta:
        model = Imagem
        fields = ['imagem']