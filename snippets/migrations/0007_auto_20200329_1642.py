# Generated by Django 2.1.1 on 2020-03-29 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0006_auto_20200329_1606'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='End_Date',
            new_name='enddate',
        ),
        migrations.RenameField(
            model_name='activity',
            old_name='Start_Date',
            new_name='startdate',
        ),
        migrations.RenameField(
            model_name='activity',
            old_name='U_ID',
            new_name='uid',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='NId',
            new_name='nid',
        ),
    ]
