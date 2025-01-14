# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-19 07:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esign_app', '0011_auto_20180119_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appversion',
            name='description',
            field=models.CharField(max_length=500, verbose_name='描述'),
        ),
        migrations.AlterField(
            model_name='appversion',
            name='url',
            field=models.CharField(max_length=500, verbose_name='下载地址'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='join_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 19, 15, 57, 2, 705686), verbose_name='加入时间'),
        ),
        migrations.AlterField(
            model_name='sign',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 19, 15, 57, 2, 708835), verbose_name='创建时间'),
        ),
    ]
