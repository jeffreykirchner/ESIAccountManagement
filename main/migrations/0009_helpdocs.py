# Generated by Django 3.2.7 on 2021-09-03 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20210903_1926'),
    ]

    operations = [
        migrations.CreateModel(
            name='HelpDocs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=300, verbose_name='Title')),
                ('path', models.CharField(default='/', max_length=300, verbose_name='URL Path')),
                ('text', models.CharField(default='', max_length=10000, verbose_name='Help Doc Text')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Help Doc',
                'verbose_name_plural': 'Help Docs',
            },
        ),
    ]
