# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-29 03:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esign_app', '0002_auto_20171229_0226'),
    ]

    operations = [
        migrations.AddField(
            model_name='documents',
            name='img_url',
            field=models.CharField(max_length=300, null=True, verbose_name='图片地址'),
        ),
        migrations.AlterField(
            model_name='documents',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 29, 3, 10, 27, 104857), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='join_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 29, 3, 10, 27, 103861), verbose_name='加入时间'),
        ),
        migrations.AlterField(
            model_name='sign',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 29, 3, 10, 27, 105645), verbose_name='创建时间'),
        ),
    ]