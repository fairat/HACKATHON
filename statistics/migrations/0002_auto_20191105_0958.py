# Generated by Django 2.2.6 on 2019-11-05 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statistics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='statistics',
            name='bus2',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='statistics',
            name='busZ',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='statistics',
            name='car2',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='statistics',
            name='carZ',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='statistics',
            name='motorbike2',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='statistics',
            name='motorbikeZ',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='statistics',
            name='truck2',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='statistics',
            name='truckZ',
            field=models.IntegerField(null=True),
        ),
    ]