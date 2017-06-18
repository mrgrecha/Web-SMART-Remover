# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Trash_bin(models.Model):
    path_of_config = models.CharField(max_length=100)
    name = models.CharField(max_length=200, primary_key=True)
    path_of_trash = models.CharField(max_length=100)
    path_of_database = models.CharField(max_length=100)
    dried = models.BooleanField()
    silent = models.BooleanField()
    size = models.BigIntegerField()
    time = models.BigIntegerField()

    def __str__(self):
        return self.name

class RegularTask(models.Model):
    regular_expression = models.CharField(max_length=200)
    start_folder = models.CharField(max_length=200)
    current_trash_bin = models.ForeignKey('Trash_bin', on_delete=models.CASCADE)

class Task(models.Model):
    pass

class File(models.Model):
    path = models.FilePathField()
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=50)
    hash_of_file = models.CharField(max_length=40)
    is_in_bin = models.BooleanField()
    size = models.BigIntegerField()
    time = models.BigIntegerField()


#             self.database = os.path.expanduser('~/.DB.json')
#             self.max_size = 500000000
#             self.max_number = 1000
#             self.max_list_height = 50
#             self.max_time = 1000
#             self.arr_json_files = serialization.load_json(self.database)
#             self.policies = 'default'
#             self.silent = False
#             self.dried = False
#             self.interactive = False
#             self.force = False