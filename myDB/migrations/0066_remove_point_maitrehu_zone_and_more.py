# Generated by Django 4.0.6 on 2022-12-30 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myDB', '0065_alter_diagnostic_causes_alter_diagnostic_plantes_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='point',
            name='maitreHu_zone',
        ),
        migrations.RemoveField(
            model_name='point',
            name='maitreTung_zone',
        ),
        migrations.AlterField(
            model_name='pathologiecause',
            name='cause',
            field=models.CharField(blank='', max_length=2000, null=True, verbose_name='Cause'),
        ),
        migrations.AlterField(
            model_name='pathologiecause',
            name='principe_therapeutique',
            field=models.CharField(blank='', max_length=2000, null=True, verbose_name='Principe therapeutique'),
        ),
        migrations.CreateModel(
            name='Point_PointZone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myDB.point')),
                ('pointZone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myDB.pointzone')),
            ],
        ),
    ]