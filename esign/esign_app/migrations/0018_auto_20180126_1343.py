# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-26 05:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esign_app', '0017_auto_20180125_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='join_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 26, 13, 43, 0, 290084), verbose_name='加入时间'),
        ),
        migrations.AlterField(
            model_name='sign',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 26, 13, 43, 0, 293261), verbose_name='创建时间'),
        ),
    ]