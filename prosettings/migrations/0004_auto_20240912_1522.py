# Generated by Django 3.2.15 on 2024-09-12 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prosettings', '0003_auto_20240912_1307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='organization',
        ),
        migrations.AddField(
            model_name='player',
            name='game',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='players_for_game', to='prosettings.game'),
        ),
        migrations.AlterField(
            model_name='team',
            name='game',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teams_for_game', to='prosettings.game'),
        ),
        migrations.DeleteModel(
            name='Organization',
        ),
    ]
