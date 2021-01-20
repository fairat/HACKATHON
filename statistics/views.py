# -*- coding: utf-8 -*-
import os
import requests
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.db.models import Sum
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import AZSSerializer
from .models import Statistics, Buyer, AZS


@api_view(["GET"])
def get_all_azs(request):
    all_azs = AZS.objects.all()
    serializer = AZSSerializer(all_azs, many=True)
    return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)


@api_view(["POST"])
def get_years(request):
    if not "azs_id" in request.data:
        return JsonResponse({"error": "not azs_id"},
                            status=status.HTTP_400_BAD_REQUEST, safe=False)
    azs = get_object_or_404(AZS, id=request.data["azs_id"])

    if not "years" in request.data or not request.data["years"]:
        years = list(Statistics.objects.filter(azs=azs).distinct().values_list("year", flat=True))
    else:
        years = request.data["years"]
    ret=[]
    for year in years:
        months = list(Statistics.objects.filter(azs=azs,
                                                year=year).order_by('month').distinct().values_list("month", flat=True))
        months_stat=[]
        for month in months:
            stat = Statistics.objects.filter(azs=azs,
                                             year=year,
                                             month=month).aggregate(Sum('count'),
                                                                    Sum('count2'),
                                                                    Sum('countz'),
                                                                    Sum('car'),
                                                                    Sum('car2'),
                                                                    Sum('carz'),
                                                                    Sum('truck'),
                                                                    Sum('truck2'),
                                                                    Sum('truckz'),
                                                                    Sum('bus'),
                                                                    Sum('bus2'),
                                                                    Sum('busz'),
                                                                    Sum('motorbike'),
                                                                    Sum('motorbike2'),
                                                                    Sum('motorbikez'))
            months_stat.append({'month': month, 'stat': stat})
        ret.append({'year': year, "months": months_stat})
    return JsonResponse(ret, status=status.HTTP_200_OK, safe=False)


@api_view(["POST"])
def get_months(request):
    if not "azs_id" in request.data or not "year" in request.data:
        return JsonResponse({"error": "not 'azs_id' or 'year'"},
                            status=status.HTTP_400_BAD_REQUEST, safe=False)
    azs = get_object_or_404(AZS, id=request.data["azs_id"])
    year = request.data["year"]
    if not "months" in request.data or not request.data["months"]:
        months = list(Statistics.objects.filter(azs=azs, year=year).distinct().values_list("month", flat=True))
    else:
        months = request.data["months"]
    ret=[]
    for month in months:
        days = list(Statistics.objects.filter(azs=azs,
                                              month=month,
                                              year=year).order_by('day').distinct().values_list("day", flat=True))
        days_stat=[]
        for day in days:
            stat = Statistics.objects.filter(azs=azs,
                                             year=year,
                                             month=month,
                                             day=day).aggregate(Sum('count'),
                                                                Sum('count2'),
                                                                Sum('countz'),
                                                                Sum('car'),
                                                                Sum('car2'),
                                                                Sum('carz'),
                                                                Sum('truck'),
                                                                Sum('truck2'),
                                                                Sum('truckz'),
                                                                Sum('bus'),
                                                                Sum('bus2'),
                                                                Sum('busz'),
                                                                Sum('motorbike'),
                                                                Sum('motorbike2'),
                                                                Sum('motorbikez'))
            days_stat.append({'day': day, 'stat': stat})
        ret.append({'year': year, "month": month, "stat":days_stat})
    return JsonResponse(ret, status=status.HTTP_200_OK, safe=False)

@api_view(["POST"])
def get_days(request):
    if not "azs_id" in request.data or not "year" in request.data or not "month" in request.data:
        return JsonResponse({"error": "not 'azs_id' or 'year' or 'month'"},
                            status=status.HTTP_400_BAD_REQUEST, safe=False)
    azs = get_object_or_404(AZS, id=request.data["azs_id"])
    year = request.data["year"]
    month = request.data["month"]
    if not "days" in request.data or not request.data["days"]:
        days = list(Statistics.objects.filter(azs=azs, year=year, month=month).distinct().values_list("day", flat=True))
    else:
        days = request.data["days"]
    ret=[]
    for day in days:
        hours = list(Statistics.objects.filter(azs=azs,
                                               year=year,
                                               month=month,
                                               day=day).order_by('hour').distinct().values_list("hour", flat=True))
        hours_stat=[]
        for hour in hours:
            stat = Statistics.objects.filter(azs=azs,
                                             year=year,
                                             month=month,
                                             day=day,
                                             hour=hour).aggregate(Sum('count'),
                                                                Sum('count2'),
                                                                Sum('countz'),
                                                                Sum('car'),
                                                                Sum('car2'),
                                                                Sum('carz'),
                                                                Sum('truck'),
                                                                Sum('truck2'),
                                                                Sum('truckz'),
                                                                Sum('bus'),
                                                                Sum('bus2'),
                                                                Sum('busz'),
                                                                Sum('motorbike'),
                                                                Sum('motorbike2'),
                                                                Sum('motorbikez'))
            filename = F"{azs.company+azs.name}_{year}-{month:02d}-{day:02d}_{hour:02d}.mp4"
            hours_stat.append({'hour': hour,
                               'stat': stat,
                               'video': filename if os.path.exists(os.path.join("media",filename)) else '' })

        ret.append({'year': year, "month": month, "day":day, "stat":hours_stat})
    return JsonResponse(ret, status=status.HTTP_200_OK, safe=False)

#---------------------------------------------------------buyer

@api_view(["POST"])
def buyer_years(request):
    if not "azs_id" in request.data:
        return JsonResponse({"error": "not azs_id"},
                            status=status.HTTP_400_BAD_REQUEST, safe=False)
    azs = get_object_or_404(AZS, id=request.data["azs_id"])

    if not "years" in request.data or not request.data["years"]:
        years = list(Buyer.objects.filter(azs=azs).distinct().values_list("year", flat=True))
    else:
        years = request.data["years"]
    ret=[]
    for year in years:
        months = list(Buyer.objects.filter(azs=azs,
                                           year=year).order_by('month').distinct().values_list("month", flat=True))
        months_stat=[]
        for month in months:
            stat = Buyer.objects.filter(azs=azs,
                                        year=year,
                                        month=month).aggregate(Sum('count'),
                                                               Sum('au92'),
                                                               Sum('au95'),
                                                               Sum('au100'),
                                                               Sum('eda'),
                                                               Sum('napit'),
                                                               Sum('soput'),
                                                               Sum('sigarets'))
            months_stat.append({'month': month, 'stat': stat})
        ret.append({'year': year, "months": months_stat})
    return JsonResponse(ret, status=status.HTTP_200_OK, safe=False)


@api_view(["POST"])
def buyer_months(request):
    if not "azs_id" in request.data or not "year" in request.data:
        return JsonResponse({"error": "not 'azs_id' or 'year'"},
                            status=status.HTTP_400_BAD_REQUEST, safe=False)
    azs = get_object_or_404(AZS, id=request.data["azs_id"])
    year = request.data["year"]
    if not "months" in request.data or not request.data["months"]:
        months = list(Buyer.objects.filter(azs=azs, year=year).distinct().values_list("month", flat=True))
    else:
        months = request.data["months"]
    ret=[]
    for month in months:
        days = list(Buyer.objects.filter(azs=azs,
                                              month=month,
                                              year=year).order_by('day').distinct().values_list("day", flat=True))
        days_stat=[]
        for day in days:
            stat = Buyer.objects.filter(azs=azs,
                                             year=year,
                                             month=month,
                                             day=day).aggregate(Sum('count'),
                                                                Sum('au92'),
                                                                Sum('au95'),
                                                                Sum('au100'),
                                                                Sum('eda'),
                                                                Sum('napit'),
                                                                Sum('soput'),
                                                                Sum('sigarets'))

            days_stat.append({'day': day, 'stat': stat})
        ret.append({'year': year, "month": month, "stat":days_stat})
    return JsonResponse(ret, status=status.HTTP_200_OK, safe=False)

@api_view(["POST"])
def buyer_days(request):
    if not "azs_id" in request.data or not "year" in request.data or not "month" in request.data:
        return JsonResponse({"error": "not 'azs_id' or 'year' or 'month'"},
                            status=status.HTTP_400_BAD_REQUEST, safe=False)
    azs = get_object_or_404(AZS, id=request.data["azs_id"])
    year = request.data["year"]
    month = request.data["month"]
    if not "days" in request.data or not request.data["days"]:
        days = list(Buyer.objects.filter(azs=azs, year=year, month=month).distinct().values_list("day", flat=True))
    else:
        days = request.data["days"]
    ret=[]
    for day in days:
        hours = list(Buyer.objects.filter(azs=azs,
                                          year=year,
                                          month=month,
                                          day=day).order_by('hour').distinct().values_list("hour", flat=True))
        hours_stat=[]
        for hour in hours:
            stat = Buyer.objects.filter(azs=azs,
                                         year=year,
                                         month=month,
                                         day=day,
                                         hour=hour).aggregate(Sum('count'),
                                                              Sum('au92'),
                                                              Sum('au95'),
                                                              Sum('au100'),
                                                              Sum('eda'),
                                                              Sum('napit'),
                                                              Sum('soput'),
                                                              Sum('sigarets'))
            filename = F"{azs.company+azs.name}_{year}-{month:02d}-{day:02d}_{hour:02d}.mp4"
            hours_stat.append({'hour': hour,
                               'stat': stat,
                               'video': filename if os.path.exists(os.path.join("media",filename)) else '' })

        ret.append({'year': year, "month": month, "day":day, "stat":hours_stat})
    return JsonResponse(ret, status=status.HTTP_200_OK, safe=False)


@api_view(["POST"])
def buyer_graph(request):

    ret = { 'count': [],
            'au92': [],
            'au95':[],
            'au100':[],
            'eda':[],
            'napit':[],
            'soput':[],
            'sigarets':[]
        }
    if not "azs_id" in request.data:
        return JsonResponse({"error": "not 'azs_id'"},
                            status=status.HTTP_400_BAD_REQUEST, safe=False)
    azs = get_object_or_404(AZS, id=request.data["azs_id"])
    year = request.data["year"] if "year" in request.data else None
    month = request.data["month"] if "month" in request.data else None
    day = request.data["day"] if "day" in request.data else None
    hour = request.data["hour"] if "hour" in request.data else None

    if not year: # За годы
        xxx = list(Buyer.objects.filter(azs=azs).order_by("year").distinct().values_list("year", flat=True))
    elif not month:
        xxx = list(Buyer.objects.filter(azs=azs,
                                        year=year).order_by("month").distinct().values_list("month", flat=True))
    elif not day:
        xxx = list(Buyer.objects.filter(azs=azs,
                                        year=year,
                                        month=month).order_by("day").distinct().values_list("day", flat=True))
    elif not hour:
        xxx = list(Buyer.objects.filter(azs=azs,
                                        year=year,
                                        month=month,
                                        day=day).order_by("hour").distinct().values_list("hour", flat=True))
    elif hour:
        xxx = list(Buyer.objects.filter(azs=azs,
                                        year=year,
                                        month=month,
                                        day=day,
                                        hour=hour).order_by("minute").distinct().values_list("minute", flat=True))
    else:
        return JsonResponse({"error": "not 'year', 'month', 'day', 'hour'"},
                            status=status.HTTP_400_BAD_REQUEST, safe=False)

    ret.update({"chartx": xxx})
    for x in xxx:
        if not year: # За годы
            filter = Buyer.objects.filter(azs=azs,
                                          year=x)
        elif not month:
            filter = Buyer.objects.filter(azs=azs,
                                          year=year,
                                          month=x)
        elif not day:
            filter = Buyer.objects.filter(azs=azs,
                                          year=year,
                                          month=month,
                                          day=x)
        elif not hour:
            filter = Buyer.objects.filter(azs=azs,
                                          year=year,
                                          month=month,
                                          day=day,
                                          hour=x)
        elif hour:
            filter = Buyer.objects.filter(azs=azs,
                                          year=year,
                                          month=month,
                                          day=day,
                                          hour=hour,
                                          minute=x)
        stat = filter.aggregate( Sum('count'),
                                 Sum('au92'),
                                 Sum('au95'),
                                 Sum('au100'),
                                 Sum('eda'),
                                 Sum('napit'),
                                 Sum('soput'),
                                 Sum('sigarets'))
        ret['count'].append(stat['count__sum'])
        ret['au92'].append(stat['au92__sum'])
        ret['au95'].append(stat['au95__sum'])
        ret['au100'].append(stat['au100__sum'])
        ret['eda'].append(stat['eda__sum'])
        ret['napit'].append(stat['napit__sum'])
        ret['soput'].append(stat['soput__sum'])
        ret['sigarets'].append(stat['sigarets__sum'])
    return JsonResponse(ret, status=status.HTTP_200_OK, safe=False)
