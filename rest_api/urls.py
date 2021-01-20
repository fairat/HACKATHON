from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from rest_api.views import change_password

from .views import UserListAPIView


urlpatterns = [
    url(r'api/v1/auth/login/', obtain_jwt_token, name='obtain_jwt_token'),
    url(r'api/v1/token/obtain/', obtain_jwt_token),
    url(r'api/v1/users/', UserListAPIView.as_view()),
    url(r"api/v1/auth/change-password/", change_password, name='auth-change-password'),
]
