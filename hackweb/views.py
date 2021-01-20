# -*- coding: utf-8 -*-

from datetime import datetime
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from hackweb.models import Anketa, Company


@api_view(["POST"])
def put_anketa(request):
    if not "number" in request.data or not "serial" in request.data:
        return JsonResponse({"error": "not number or serial"},
                            status=status.HTTP_400_BAD_REQUEST, safe=False)

    if Anketa.objects.filter(number=request.data["number"],
                             serial=request.data["serial"]).exists():
        return JsonResponse(
            {"error": "Регистрация с " + request.data["serial"] + " " + request.data["number"] +
             " уже произведена."},
            status=status.HTTP_400_BAD_REQUEST, safe=False)

    a = Anketa()
    a.aboutme = request.data["aboutme"]
    a.inputDate = request.data["inputDate"]
    a.middlename = request.data["middlename"]
    a.name = request.data["name"]
    a.number = request.data["number"]
    a.release = request.data["release"]
    a.serial = request.data["serial"]
    a.specialty = request.data["specialty"]
    a.surname = request.data["surname"]
    a.who = request.data["who"]
    a.whyme = request.data["whyme"]
    a.create_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    ret = a.save()
    return JsonResponse(ret, status=status.HTTP_200_OK, safe=False)


@api_view(["POST"])
def put_company(request):
    if not "name" in request.data or not "fio" in request.data:
        return JsonResponse({"error": "not company name or fio"},
                            status=status.HTTP_400_BAD_REQUEST, safe=False)

    if Anketa.objects.filter(number=request.data["name"]).exists():
        return JsonResponse(
            {"error": "Регистрация " + request.data["name"] + " уже произведена."},
            status=status.HTTP_400_BAD_REQUEST, safe=False)

    a = Company()
    a.name = request.data["name"]
    a.inn = request.data["inn"]
    a.fio = request.data["fio"]
    a.position = request.data["position"]
    a.telephon = request.data["telephon"]
    a.email = request.data["email"]
    a.task1 = request.data["task1"]
    a.task2 = request.data["task2"]
    a.task3 = request.data["task3"]
    a.task4 = request.data["task4"]
    a.task5 = request.data["task5"]
    a.create_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    ret = a.save()
    return JsonResponse(ret, status=status.HTTP_200_OK, safe=False)
