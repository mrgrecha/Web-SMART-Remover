# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-23 18:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smart_rm', '0018_task_hashes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='history',
            name='regular_task',
        ),
        migrations.RemoveField(
            model_name='history',
            name='task',
        ),
        migrations.AddField(
            model_name='history',
            name='files',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='history',
            name='pattern',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='history',
            name='start_folder',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='history',
            name='trash_bin',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='hashes',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
