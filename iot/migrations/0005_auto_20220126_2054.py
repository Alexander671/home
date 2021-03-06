# Generated by Django 3.2 on 2022-01-26 17:54

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('iot', '0004_auto_20220126_2035'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(default='', max_length=300)),
                ('time_request', models.DateTimeField(default=datetime.datetime(2022, 1, 26, 17, 54, tzinfo=utc))),
                ('response', models.TextField(null=True)),
                ('description', models.CharField(max_length=300, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Request',
                'verbose_name_plural': 'Requests',
            },
        ),
        migrations.DeleteModel(
            name='IoTModel',
        ),
    ]
