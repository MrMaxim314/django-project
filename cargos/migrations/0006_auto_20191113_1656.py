# Generated by Django 2.2.6 on 2019-11-13 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cargos', '0005_transfer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cargo',
            name='cargo_weight',
            field=models.IntegerField(max_length=7),
        ),
    ]
