# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-22 01:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0042_auto_20170715_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='auction_date_end',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='auction_date_start',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
