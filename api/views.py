from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Empreendimeto
from .serializer import EmpreendimentoSerializer


class EmpreendimentoView(APIView):
    permission_classes = (IsAuthenticated,)


    def get(self, request):
        empreendimentos = Empreendimeto.objects.all()
        serializer = EmpreendimentoSerializer(empreendimentos, many=True)
        return Response(serializer.data)