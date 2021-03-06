# Generated by Django 2.2.6 on 2019-11-05 06:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AZS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('company', models.CharField(max_length=500)),
                ('region', models.CharField(max_length=500)),
            ],
            options={
                'unique_together': {('name', 'company')},
            },
        ),
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(null=True)),
                ('month', models.IntegerField(null=True)),
                ('day', models.IntegerField(null=True)),
                ('hour', models.IntegerField(null=True)),
                ('minute', models.IntegerField(null=True)),
                ('car', models.IntegerField(null=True)),
                ('truck', models.IntegerField(null=True)),
                ('bus', models.IntegerField(null=True)),
                ('motorbike', models.IntegerField(null=True)),
                ('azs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='statistics.AZS')),
            ],
        ),
    ]
