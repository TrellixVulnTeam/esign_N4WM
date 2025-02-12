# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-01 07:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esign_app', '0021_auto_20180131_1045'),
    ]

    operations = [
        migrations.AddField(
            model_name='financingcontract',
            name='contract_type',
            field=models.CharField(max_length=20, null=True, verbose_name='合同种类'),
        ),
        migrations.AddField(
            model_name='financingcontract',
            name='pay_method',
            field=models.CharField(default='1', max_length=2, verbose_name='付款方式'),
        ),
        migrations.AlterField(
            model_name='contract_demo',
            name='demo_type',
            field=models.CharField(default='trade_contract', max_length=300, verbose_name='模版类型'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='join_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 1, 15, 47, 43, 243862), verbose_name='加入时间'),
        ),
        migrations.AlterField(
            model_name='sign',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 1, 15, 47, 43, 247056), verbose_name='创建时间'),
        ),
    ]
