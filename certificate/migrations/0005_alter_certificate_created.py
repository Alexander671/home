# Generated by Django 3.2 on 2022-02-02 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificate', '0004_alter_certificate_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='created',
            field=models.DateField(default='2022-02-02'),
        ),
    ]
