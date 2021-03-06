# Generated by Django 3.1.2 on 2020-10-25 13:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("data_mine", "0002_initial_populate"),
    ]

    operations = [
        migrations.CreateModel(
            name="MemeTemplateToGameThrough",
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
                    "order",
                    models.PositiveSmallIntegerField(
                        help_text="The order-by field per-game. You can have the same ordering value for memes but this may have unpredictable results. This field is automatically set to N+1 if left as 0."
                    ),
                ),
            ],
            options={
                "ordering": ["order"],
            },
        ),
        migrations.AlterField(
            model_name="memetemplate",
            name="dislikes",
            field=models.PositiveIntegerField(
                default=0,
                help_text="The number of times this template has been disliked.",
            ),
        ),
        migrations.AlterField(
            model_name="memetemplate",
            name="likes",
            field=models.PositiveIntegerField(
                default=0, help_text="The number of times this template has been liked."
            ),
        ),
    ]
