# Generated by Django 5.0.3 on 2024-07-16 13:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0001_initial"),
        ("locations", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="location",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="locations.city",
            ),
        ),
    ]