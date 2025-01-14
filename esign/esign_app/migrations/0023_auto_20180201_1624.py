# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-01 08:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esign_app', '0022_auto_20180201_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='financingcontract',
            name='contract_type',
            field=models.CharField(max_length=30, null=True, verbose_name='合同种类'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='join_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 1, 16, 24, 40, 300036), verbose_name='加入时间'),
        ),
        migrations.AlterField(
            model_name='sign',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 1, 16, 24, 40, 302008), verbose_name='创建时间'),
        ),
    ]
