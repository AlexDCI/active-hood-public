# Generated by Django 3.2.25 on 2024-07-18 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_alter_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='friends',
            field=models.ManyToManyField(blank=True, related_name='_users_profile_friends_+', to='users.Profile'),
        ),
    ]
