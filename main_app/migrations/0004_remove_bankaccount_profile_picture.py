# Generated by Django 4.1.3 on 2022-11-25 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_bankaccount_profile_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bankaccount',
            name='profile_picture',
        ),
    ]
