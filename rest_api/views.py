from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm

from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from .serializers import UserSerializer


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['POST'])
def change_password(request: "Request"):
    """
    Функция для смены пароля, с вводом старого пароля.
    На вход должен поступать словарь с данными:
    {"old_password": "old_pass", "new_password1": "new_pass", "new_password2": "newpass}

    При успешной смене пароля осуществляется логаут и перенаправление на страницу входа.

    Ошибки возвращаются в формате:
    {"error":
        {
            "error_messages": {
                "password_missmath": "some text",
                "password_incorrect": "some text",
                }
            "errors_fields": {
                "old_password": [
                    "some text",
                ],
                "new_password1": [
                    "some text",
                ],
                "new_password2": [
                    "some text",
                ]},
        }
    }

    """
    form = PasswordChangeForm(user=request.user, data=request.data)
    if form.is_valid():
        form.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response({"error": {"error_messages": form.error_messages,
                               "errors_fields": form.errors,},}, status=status.HTTP_400_BAD_REQUEST)
