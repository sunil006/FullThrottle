# Generated by Django 2.1.1 on 2020-03-29 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0004_auto_20200329_1058'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['NId']},
        ),
        migrations.RemoveField(
            model_name='user',
            name='sm',
        ),
        migrations.AddField(
            model_name='activity',
            name='U_ID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='snippets.User'),
            preserve_default=False,
        ),
    ]