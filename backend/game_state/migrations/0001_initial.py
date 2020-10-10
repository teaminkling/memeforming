# Generated by Django 3.1 on 2020-08-16 07:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Game",
            fields=[
                (
                    "room_key",
                    models.CharField(
                        help_text="The unique room key.",
                        max_length=4,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                (
                    "game_started_timestamp",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="The timestamp of the room's creation, used to calculate when the room should be deleted.",
                    ),
                ),
                (
                    "state",
                    models.CharField(
                        choices=[
                            ("Creating Game Room", "Creating Game Room"),
                            ("Waiting for Players", "Waiting for Players"),
                            ("Forging Memes", "Forging Memes"),
                            ("Judging Memes", "Judging Memes"),
                            ("Presenting Winners", "Presenting Winners"),
                        ],
                        default="Creating Game Room",
                        help_text="The current state of the game.",
                        max_length=64,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Player",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="A player's chosen name.", max_length=256
                    ),
                ),
                (
                    "game",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="game_state.game",
                    ),
                ),
            ],
            options={"unique_together": {("game", "name")}, },
        ),
    ]
