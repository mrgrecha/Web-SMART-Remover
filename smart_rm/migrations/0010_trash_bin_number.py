# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-20 20:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smart_rm', '0009_auto_20170620_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='trash_bin',
            name='number',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
    ]