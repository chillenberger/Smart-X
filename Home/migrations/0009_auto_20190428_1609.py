# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-04-28 20:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0008_auto_20190428_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippinginfomodel',
            name='creationDate',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 28, 16, 9, 49, 224561)),
        ),
    ]