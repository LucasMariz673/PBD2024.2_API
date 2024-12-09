from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from .settings import MEDIA_URL, MEDIA_ROOT

from api.views import EmpreendimentoView, EmpreendimentoUpdateDetailAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenVerifyView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/validation/', TokenVerifyView.as_view(), name='token_validation'),
    path('api/v1/empreendimento/', EmpreendimentoView.as_view(), name='empreendimentos'),
    path('api/empreendimento/<int:pk>/', EmpreendimentoUpdateDetailAPIView.as_view(), name='empreendimento-update'),

] + static(MEDIA_URL, document_root = MEDIA_ROOT)