# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-10 09:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esign_app', '0007_auto_20180108_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='birthday',
            field=models.CharField(max_length=20, null=True, verbose_name='生日'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='region',
            field=models.CharField(max_length=32, null=True, verbose_name='地区'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='sex',
            field=models.CharField(default='男', max_length=10, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='join_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 10, 17, 46, 53, 934371), verbose_name='加入时间'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='level',
            field=models.CharField(default='free', max_length=32, verbose_name='等级'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='total_capacity',
            field=models.FloatField(default=5000000, verbose_name='容量'),
        ),
        migrations.AlterField(
            model_name='sign',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 10, 17, 46, 53, 937830), verbose_name='创建时间'),
        ),
    ]
