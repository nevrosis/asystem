# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-05 00:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0018_itempicture_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='itempicture',
            name='item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auctions.Item', verbose_name='Item'),
        ),
    ]