# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-22 20:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smart_rm', '0014_history_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='regular_task',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='smart_rm.RegularTask'),
        ),
        migrations.AlterField(
            model_name='history',
            name='task',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='smart_rm.Task'),
        ),
    ]
