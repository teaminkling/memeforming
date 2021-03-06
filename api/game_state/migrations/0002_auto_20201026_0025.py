# Generated by Django 3.1.2 on 2020-10-25 13:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("game_state", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="game",
            name="vip",
            field=models.ForeignKey(
                blank=True,
                help_text="The VIP of this game that can modify the settings. If not set, it will eventually be deleted by the system.",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="game_vip_player",
                to="game_state.player",
                verbose_name="VIP",
            ),
        ),
    ]
