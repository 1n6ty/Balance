# Generated by Django 4.0.2 on 2023-09-06 18:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Balance', '0004_alter_purchases_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchases',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 6, 18, 31, 47, 863242, tzinfo=utc), verbose_name='Время'),
        ),
    ]
