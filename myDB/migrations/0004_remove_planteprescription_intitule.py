# Generated by Django 4.0.6 on 2022-08-08 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myDB', '0003_planteprescription_intitule_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planteprescription',
            name='intitule',
        ),
    ]
