# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-02 03:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_auctioneer_motto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auctioneer',
            old_name='active',
            new_name='activated',
        ),
    ]