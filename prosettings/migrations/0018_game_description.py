# Generated by Django 3.2.16 on 2024-11-01 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prosettings', '0017_game_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
