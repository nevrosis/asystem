# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-05 01:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0021_auto_20170705_0101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itempicture',
            name='name',
            field=models.CharField(default='', max_length=256, null=True, verbose_name='Name'),
        ),
    ]
