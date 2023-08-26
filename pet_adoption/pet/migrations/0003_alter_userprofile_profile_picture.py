# Generated by Django 4.2.4 on 2023-08-26 09:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pet", "0002_alter_adoptionstory_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="profile_picture",
            field=models.ImageField(
                blank=True,
                default="profile_pics/default.jpg",
                null=True,
                upload_to="profile_pics/",
            ),
        ),
    ]
