# Generated by Django 2.2.6 on 2019-11-05 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('statistics', '0003_auto_20191105_1237'),
    ]

    operations = [
        migrations.RenameField(
            model_name='statistics',
            old_name='busZ',
            new_name='busz',
        ),
        migrations.RenameField(
            model_name='statistics',
            old_name='carZ',
            new_name='carz',
        ),
        migrations.RenameField(
            model_name='statistics',
            old_name='countZ',
            new_name='countz',
        ),
        migrations.RenameField(
            model_name='statistics',
            old_name='motorbikeZ',
            new_name='motorbikez',
        ),
        migrations.RenameField(
            model_name='statistics',
            old_name='truckZ',
            new_name='truckz',
        ),
    ]
