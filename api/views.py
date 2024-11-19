from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


"""class LoginAPIView(APIView):


    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")


        user = authenticate(username=username, password=password)

        if user:
            return Response({"message": "Login bem-sucedido!", "username": user.username}, status=status.HTTP_200_OK)
        return Response({"error": "Credenciais inválidas!"}, status=status.HTTP_400_BAD_REQUEST)
"""