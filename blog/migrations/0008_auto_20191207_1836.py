# Generated by Django 2.2.7 on 2019-12-07 13:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20191207_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 7, 13, 6, 43, 27943, tzinfo=utc)),
        ),
    ]
