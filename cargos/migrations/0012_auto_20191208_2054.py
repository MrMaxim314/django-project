# Generated by Django 2.2.6 on 2019-12-08 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cargos', '0011_auto_20191208_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto',
            name='data_back',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='auto',
            name='data_rent',
            field=models.DateField(),
        ),
    ]