# Generated by Django 2.2.6 on 2019-12-10 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cargos', '0019_delete_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=70)),
                ('mark', models.CharField(max_length=77)),
                ('days', models.IntegerField()),
                ('total_price', models.IntegerField()),
            ],
        ),
    ]
