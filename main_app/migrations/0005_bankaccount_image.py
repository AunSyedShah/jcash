# Generated by Django 4.1.3 on 2022-11-27 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_remove_bankaccount_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankaccount',
            name='image',
            field=models.ImageField(default='images/default.png', upload_to='images/'),
        ),
    ]
