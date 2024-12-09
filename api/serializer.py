from rest_framework import serializers
from .models import Empreendimento, Imagem

class ImagenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Imagem
        fields = ['imagem']

class EmpreendimentoSerializer(serializers.ModelSerializer):
    imagens = ImagenSerializer(many=True, read_only=True)
    imagens_upload = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True
    )

    class Meta:
        model = Empreendimento
        fields = ['nome',
                  'endereco',
                  'total_lotes',
                  'total_disponivel',
                  'imagens',
                  'imagens_upload'
                 ]

    def create(self, validated_data):
        imagens_data = validated_data.pop('imagens_upload')
        empreendimento = Empreendimento.objects.create(
            nome=validated_data['nome'],
            endereco=validated_data['endereco'])

        for imagem_data in imagens_data:
            Imagem.objects.create(empreendimento=empreendimento, imagem=imagem_data)

        return empreendimento

    def update(self, instance, validated_data):
        imagens_data = validated_data.pop('imagens_upload', None)

        instance.nome = validated_data.get('nome', instance.nome)
        instance.endereco = validated_data.get('endereco', instance.endereco)
        instance.save()

        if imagens_data is not None:
            instance.imagens.all().delete()
            for imagem_data in imagens_data:
                Imagem.objects.create(empreendimento=instance, imagem=imagem_data)

        return instance