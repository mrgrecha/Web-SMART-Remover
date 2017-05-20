# -*- coding: utf-8 -*-
import uuid
import time
import os


class FileObject(object):
    """A class of file in Smart RM """
    def __init__(self):
        self.path = ''
        self.time_of_life = 0
        self.name = ''
        self.type = ''
        self.hash = 0
        self.size = 0
        self.IsInBin = False      # if bin has this file = true. else = false

    def make_object(self, name):
        self.name = name.split('/')[-1]
        self.path = os.path.abspath(name)
        self.time_of_life = time.time()
        self.size = os.path.getsize(name)
        self.hash = str(uuid.uuid4())
        self.IsInBin = True

    def make_from_json(self, path, time, name, type, hash, state, size):
        self.path = path
        self.time_of_life = time
        self.name = name
        self.type = type
        self.hash = hash
        self.IsInBin = state
        self.size = size

    def set_type(self, kind):
        self.type = kind

    def make_from_dict(self, some_dict):
        self.path = some_dict['path']
        self.time_of_life = some_dict['time_of_life']
        self.name = some_dict['name']
        self.type = some_dict['type']
        self.hash = some_dict['hash']
        self.IsInBin = some_dict['IsInBin']
        self.size = some_dict['size']

        # ini-file ;для читаемости

