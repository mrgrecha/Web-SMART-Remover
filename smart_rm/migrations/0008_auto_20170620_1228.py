# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-20 09:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smart_rm', '0007_auto_20170618_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='files_to_delete',
            field=models.CharField(max_length=100000),
        ),
    ]