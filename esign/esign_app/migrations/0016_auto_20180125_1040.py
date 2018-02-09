# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-25 02:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esign_app', '0015_auto_20180124_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='documents',
            name='document_type',
            field=models.CharField(default='trade_contract', max_length=20, verbose_name='文档类型'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='join_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 25, 10, 40, 39, 906916), verbose_name='加入时间'),
        ),
        migrations.AlterField(
            model_name='sign',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 25, 10, 40, 39, 908570), verbose_name='创建时间'),
        ),
    ]