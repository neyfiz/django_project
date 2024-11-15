# Generated by Django 3.2.15 on 2024-09-12 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prosettings', '0005_auto_20240912_1609'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='team',
        ),
        migrations.AddField(
            model_name='player',
            name='games',
            field=models.ManyToManyField(blank=True, related_name='players', to='prosettings.Game'),
        ),
        migrations.AddField(
            model_name='player',
            name='teams',
            field=models.ManyToManyField(blank=True, related_name='players', to='prosettings.Team'),
        ),
    ]
