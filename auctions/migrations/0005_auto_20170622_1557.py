# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-22 15:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_auto_20170620_2143'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='terminated',
            field=models.BooleanField(default=False, verbose_name='Terminated'),
        ),
        migrations.AddField(
            model_name='auction',
            name='terminated_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date terminated'),
        ),
    ]
