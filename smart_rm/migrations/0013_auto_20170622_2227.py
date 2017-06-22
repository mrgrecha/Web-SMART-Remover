# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-22 19:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smart_rm', '0012_history'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='history',
            name='text',
        ),
        migrations.AddField(
            model_name='history',
            name='regular_task',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='smart_rm.RegularTask'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='history',
            name='task',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='smart_rm.Task'),
            preserve_default=False,
        ),
    ]
