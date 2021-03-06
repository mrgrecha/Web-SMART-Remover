# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-30 22:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smart_rm', '0002_auto_20170525_0853'),
    ]

    operations = [
        migrations.AddField(
            model_name='trash_bin',
            name='dried',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trash_bin',
            name='name',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trash_bin',
            name='path_of_config',
            field=models.FilePathField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trash_bin',
            name='path_of_database',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trash_bin',
            name='path_of_trash',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trash_bin',
            name='silent',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trash_bin',
            name='size',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trash_bin',
            name='time',
            field=models.BigIntegerField(default=10000000000),
            preserve_default=False,
        ),
    ]
