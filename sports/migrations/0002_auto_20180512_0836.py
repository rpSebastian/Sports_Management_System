# Generated by Django 2.0.5 on 2018-05-12 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agegroup',
            name='age_id',
        ),
        migrations.RemoveField(
            model_name='athlete',
            name='athelete_id',
        ),
        migrations.RemoveField(
            model_name='project',
            name='Project_id',
        ),
        migrations.RemoveField(
            model_name='team',
            name='Team_id',
        ),
    ]
