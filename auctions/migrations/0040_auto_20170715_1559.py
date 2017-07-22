# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-15 15:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0039_auto_20170715_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='state_province',
            field=models.CharField(blank=True, choices=[('NY', 'New York'), ('QC', 'Quebec'), ('ON', 'Ontario')], max_length=2, null=True, verbose_name='State/Province'),
        ),
    ]