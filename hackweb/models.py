from django.db import models
from django.utils import timezone
# Create your models here.


class Anketa(models.Model):
    '''
    Участники
    '''
    name = models.CharField(max_length=500, null=False)
    middlename = models.CharField(max_length=500, null=False)
    aboutme = models.CharField(max_length=500, null=False)
    inputDate = models.BigIntegerField(null=True, default=0)
    number = models.CharField(max_length=500, null=False)
    release = models.CharField(max_length=500, null=False)
    serial = models.CharField(max_length=500, null=False)
    specialty = models.CharField(max_length=500, null=False)
    surname = models.CharField(max_length=500, null=False)
    who = models.CharField(max_length=500, null=False)
    whyme = models.CharField(max_length=500, null=False)
    create_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Company(models.Model):
    '''
    Компании
    '''
    name = models.CharField(max_length=500, null=False)
    inn = models.CharField(max_length=500, null=False)
    fio = models.CharField(max_length=500, null=False)
    position = models.CharField(max_length=500, null=False)
    telephon = models.CharField(max_length=500, null=False)
    email = models.CharField(max_length=500, null=False)
    task1 = models.CharField(max_length=500, null=False)
    task2 = models.CharField(max_length=500, null=False)
    task3 = models.CharField(max_length=500, null=False)
    task4 = models.CharField(max_length=500, null=False)
    task5 = models.CharField(max_length=500, null=False)
    create_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

