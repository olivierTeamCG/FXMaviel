# Generated by Django 4.0.6 on 2022-09-14 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myDB', '0049_pathologiecause_symptome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pathologiecause',
            name='symptome',
            field=models.TextField(blank='', max_length=2000, null=True, verbose_name='Symptome'),
        ),
    ]