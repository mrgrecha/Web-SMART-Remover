# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Trash_bin(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    path_of_trash = models.CharField(max_length=100)
    dried = models.BooleanField()
    silent = models.BooleanField()
    size = models.BigIntegerField()
    time = models.BigIntegerField()
    number = models.BigIntegerField()
    policies = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class RegularTask(models.Model):
    regular_expression = models.CharField(max_length=200)
    start_folder = models.CharField(max_length=200)
    current_trash_bin = models.ForeignKey('Trash_bin', on_delete=models.CASCADE)

class Task(models.Model):
    current_trash_bin = models.ForeignKey('Trash_bin', on_delete=models.CASCADE)
    files_to_delete = models.TextField()

class Log(models.Model):
    text = models.TextField()