# Generated by Django 3.2.15 on 2024-09-13 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prosettings', '0007_auto_20240913_1530'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='games',
            new_name='game',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='teams',
            new_name='team',
        ),
    ]