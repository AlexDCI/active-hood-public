# Generated by Django 5.0.3 on 2024-07-18 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0013_merge_20240717_0927"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="avatar",
            field=models.ImageField(
                default="profile_images/default.png", upload_to="profile_images/"
            ),
        ),
    ]