# Generated by Django 4.0.6 on 2022-08-19 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myDB', '0016_contact_vous_ne_transpirez_jamais_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='transpirez_vous_tres_facilement',
            field=models.BooleanField(null=True, verbose_name='Transpirez-vous très facilement, au moindre effort ?'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='vous_ne_transpirez_jamais',
            field=models.BooleanField(null=True, verbose_name='Vous ne transpirez jamais, ou pratiquement jamais ?'),
        ),
    ]
