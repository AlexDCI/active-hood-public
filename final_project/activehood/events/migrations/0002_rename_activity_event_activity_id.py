# Generated by Django 5.0.3 on 2024-07-19 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="event",
            old_name="activity",
            new_name="activity_id",
        ),
    ]
