# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-04-28 19:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_auto_20190428_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippinginfomodel',
            name='barCodeReadable',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='shippinginfomodel',
            name='creationDate',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 28, 15, 43, 46, 619003)),
        ),
        migrations.AlterField(
            model_name='shippinginfomodel',
            name='pinCode',
            field=models.CharField(blank=True, max_length=9, null=True),
        ),
    ]