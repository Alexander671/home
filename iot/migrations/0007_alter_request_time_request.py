# Generated by Django 3.2 on 2022-02-02 17:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('iot', '0006_auto_20220126_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='time_request',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 2, 17, 0, tzinfo=utc)),
        ),
    ]
