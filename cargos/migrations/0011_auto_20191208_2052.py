# Generated by Django 2.2.6 on 2019-12-08 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cargos', '0010_auto_20191208_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto',
            name='data_back',
            field=models.DateField(default='2019-05-22'),
        ),
        migrations.AlterField(
            model_name='auto',
            name='data_rent',
            field=models.DateField(default='2019-05-22'),
        ),
    ]