# Generated by Django 3.2.7 on 2021-09-08 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_rename_profile_id_profile_global_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email_confirmed',
            field=models.CharField(default='no', max_length=100, verbose_name='Email Confirmed'),
        ),
    ]
