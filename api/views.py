from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Empreendimento
from .serializer import EmpreendimentoSerializer
from rest_framework import status


class EmpreendimentoView(APIView):
    permission_classes = (IsAuthenticated,)


    def get(self, request):
        empreendimentos = Empreendimento.objects.all()
        serializer = EmpreendimentoSerializer(empreendimentos, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = EmpreendimentoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmpreendimentoUpdateDetailAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request, pk, *args, **kwargs):
        try:
            empreendimento = Empreendimento.objects.get(pk=pk)
        except Empreendimento.DoesNotExist:
            return Response({"detail": "Empreendimento não encontrado"}, status=status.HTTP_404_NOT_FOUND)

        serializer = EmpreendimentoSerializer(empreendimento, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk, *args, **kwargs):
        try:
            empreendimento = Empreendimento.objects.get(pk=pk)
            serializer = EmpreendimentoSerializer(empreendimento)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Empreendimento.DoesNotExist:
            return Response({'error': 'Empreendimento não encontrado'}, status=status.HTTP_404_NOT_FOUND)

