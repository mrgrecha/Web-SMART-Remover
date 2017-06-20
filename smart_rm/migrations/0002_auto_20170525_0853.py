# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-25 05:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smart_rm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='is_in_bin',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='file',
            name='path',
            field=models.FilePathField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='file',
            name='size',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='file',
            name='time',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
    ]