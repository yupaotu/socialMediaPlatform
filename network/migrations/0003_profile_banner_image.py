# Generated by Django 4.1.4 on 2023-02-20 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("network", "0002_alter_profile_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="banner_image",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
    ]
