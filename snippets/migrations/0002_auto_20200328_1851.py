# Generated by Django 2.1.1 on 2020-03-28 18:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='U_ID',
        ),
        migrations.AddField(
            model_name='user',
            name='End_Date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='user',
            name='Start_Date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.DeleteModel(
            name='Activity',
        ),
    ]