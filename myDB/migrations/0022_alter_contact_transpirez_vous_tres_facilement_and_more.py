# Generated by Django 4.0.6 on 2022-08-19 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myDB', '0021_contact_transpirez_vous_tres_facilement_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='transpirez_vous_tres_facilement',
            field=models.BooleanField(default=False, verbose_name='Transpirez-vous très facilement, au moindre effort ?'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='vous_ne_transpirez_jamais',
            field=models.BooleanField(default=False, verbose_name='Vous ne transpirez jamais, ou pratiquement jamais ?'),
        ),
    ]
