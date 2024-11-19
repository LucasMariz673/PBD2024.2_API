from django.contrib import admin
from django.urls import path
#from api.views import LoginAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenVerifyView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
#   path('api/login/', LoginAPIView.as_view(), name='login'),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/validation/', TokenVerifyView.as_view(), name='token_validation'),
]
