# Generated by Django 2.2.6 on 2019-12-10 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cargos', '0021_roots'),
    ]

    operations = [
        migrations.RenameField(
            model_name='roots',
            old_name='place_from',
            new_name='root',
        ),
        migrations.RemoveField(
            model_name='roots',
            name='place_to',
        ),
    ]
