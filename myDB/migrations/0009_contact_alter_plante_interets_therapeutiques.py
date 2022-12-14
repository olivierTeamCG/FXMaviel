# Generated by Django 4.0.6 on 2022-08-13 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myDB', '0008_plante_famille_plante_delete_plantefamilleplante'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('firstname', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('message', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AlterField(
            model_name='plante',
            name='interets_therapeutiques',
            field=models.TextField(blank=True, max_length=5000, null=True, verbose_name='Intérêts thérapeutiques'),
        ),
    ]
