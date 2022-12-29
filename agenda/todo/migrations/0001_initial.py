# Generated by Django 4.1.2 on 2022-12-22 18:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ToDo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField(blank=True, null=True)),
                ("date", models.DateField(default=datetime.date.today)),
                ("estimated_end", models.DateField(blank=True, null=True)),
                ("priority", models.IntegerField(default=3)),
            ],
        ),
    ]
