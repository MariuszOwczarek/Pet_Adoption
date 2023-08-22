# Generated by Django 4.0.6 on 2023-08-20 15:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0004_rename_mail_userprofile_email_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adoption',
            options={'verbose_name_plural': 'Adoptions'},
        ),
        migrations.AlterModelOptions(
            name='animal',
            options={'verbose_name_plural': 'Animals'},
        ),
        migrations.AlterModelOptions(
            name='services',
            options={'verbose_name_plural': 'Services'},
        ),
        migrations.AlterModelOptions(
            name='treatments',
            options={'verbose_name_plural': 'Treatments'},
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name_plural': 'User Profiles'},
        ),
        migrations.RenameField(
            model_name='services',
            old_name='services',
            new_name='service_name',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='surname',
            new_name='last_name',
        ),
        migrations.AlterField(
            model_name='adoption',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='animal',
            name='registration',
            field=models.DateField(default=datetime.date(2023, 8, 20)),
        ),
        migrations.AlterField(
            model_name='treatments',
            name='date',
            field=models.DateField(default=datetime.date(2023, 8, 20)),
        ),
    ]