# Generated by Django 4.0.2 on 2023-09-06 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Balance', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rates',
            name='files',
        ),
        migrations.RemoveField(
            model_name='rates',
            name='links',
        ),
        migrations.AlterField(
            model_name='purchases',
            name='date_time',
            field=models.DateTimeField(default='06.09.2023 16:30:11', verbose_name='Время'),
        ),
        migrations.DeleteModel(
            name='Files',
        ),
        migrations.DeleteModel(
            name='Links',
        ),
    ]