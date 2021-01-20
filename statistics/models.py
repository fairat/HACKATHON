from django.db import models

# Create your models here.
from django.http import Http404
from django.shortcuts import get_list_or_404, get_object_or_404


class AZS(models.Model):

    name = models.CharField(max_length=500, null=False)
    company = models.CharField(max_length=500, null=False)
    region = models.CharField(max_length=500, null=False)

    class Meta:
        unique_together = ("name", "company")

    def __str__(self):
        return self.company + " " + self.name


class Statistics(models.Model):
    """
    Таблица для сбора статистики по АЗС.
    """
    azs = models.ForeignKey("AZS", on_delete=models.CASCADE, null=False)
    year = models.IntegerField(null=True)
    month = models.IntegerField(null=True)
    day = models.IntegerField(null=True)
    hour = models.IntegerField(null=True)
    minute = models.IntegerField(null=True)
    # Total
    count = models.IntegerField(null=True)
    count2 = models.IntegerField(null=True)
    countz = models.IntegerField(null=True)
    # Line 1
    car = models.IntegerField(null=True)
    truck = models.IntegerField(null=True)
    bus = models.IntegerField(null=True)
    motorbike = models.IntegerField(null=True)
    # Line 2
    car2 = models.IntegerField(null=True)
    truck2 = models.IntegerField(null=True)
    bus2 = models.IntegerField(null=True)
    motorbike2 = models.IntegerField(null=True)
    # Line Заехало на АЗС
    carz = models.IntegerField(null=True)
    truckz = models.IntegerField(null=True)
    busz = models.IntegerField(null=True)
    motorbikez = models.IntegerField(null=True)

class Buyer(models.Model):
    """
    Таблица для сбора статистики покупателейпо АЗС.
    """
    azs = models.ForeignKey("AZS", on_delete=models.CASCADE, null=False)
    year = models.IntegerField(null=True)
    month = models.IntegerField(null=True)
    day = models.IntegerField(null=True)
    hour = models.IntegerField(null=True)
    minute = models.IntegerField(null=True)
    # Total
    count = models.IntegerField(null=True)
    # Line 1
    au92 = models.IntegerField(null=True)
    au95 = models.IntegerField(null=True)
    au100 = models.IntegerField(null=True)
    eda = models.IntegerField(null=True)
    napit = models.IntegerField(null=True)
    soput = models.IntegerField(null=True)
    sigarets = models.IntegerField(null=True)
