# Generated by Django 3.2.7 on 2021-09-07 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20210907_1619'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profile_id',
            new_name='global_id',
        ),
    ]
