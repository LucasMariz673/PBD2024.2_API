from rest_framework import serializers
from .models import Empreendimeto

class EmpreendimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empreendimeto
        fields = ['nome',
                  'total_lotes',
                  'total_disponivel'
                  ]

