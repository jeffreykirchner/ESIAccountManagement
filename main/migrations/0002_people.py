# Generated by Django 3.2.7 on 2021-09-01 23:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='Adam', max_length=1000)),
                ('last_name', models.CharField(default='Smith', max_length=1000)),
                ('email', models.EmailField(default='Adam_Smith@chapman.edu', max_length=254)),
                ('organization', models.CharField(default='Chapman University', max_length=1000)),
                ('user_name', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('password', models.CharField(default='Super Secret', max_length=1000)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'People',
                'verbose_name_plural': 'People',
            },
        ),
    ]
