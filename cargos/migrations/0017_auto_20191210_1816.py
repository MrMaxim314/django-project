# Generated by Django 2.2.6 on 2019-12-10 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cargos', '0016_auto_20191210_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='data_end',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='service',
            name='data_start',
            field=models.DateTimeField(),
        ),
    ]