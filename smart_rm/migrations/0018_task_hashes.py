# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-22 23:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smart_rm', '0017_auto_20170623_0210'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='hashes',
            field=models.TextField(blank=True, null=True),
        ),
    ]