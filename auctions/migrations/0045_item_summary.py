# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-23 04:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0044_auto_20170722_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='summary',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Summary'),
        ),
    ]