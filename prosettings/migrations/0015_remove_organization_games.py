# Generated by Django 3.2.16 on 2024-11-01 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prosettings', '0014_auto_20241101_1245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='games',
        ),
    ]
