# Generated by Django 2.2.6 on 2019-12-08 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cargos', '0009_auto_20191208_1656'),
    ]

    operations = [
        migrations.AddField(
            model_name='auto',
            name='data_back',
            field=models.DateField(default='2019-05-22'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='auto',
            name='data_rent',
            field=models.DateField(default='2019-05-22'),
            preserve_default=False,
        ),
    ]