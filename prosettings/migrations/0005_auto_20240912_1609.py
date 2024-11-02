# Generated by Django 3.2.15 on 2024-09-12 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prosettings', '0004_auto_20240912_1522'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='game',
        ),
        migrations.RemoveField(
            model_name='team',
            name='game',
        ),
        migrations.AddField(
            model_name='team',
            name='games',
            field=models.ManyToManyField(blank=True, related_name='teams', to='prosettings.Game'),
        ),
    ]
