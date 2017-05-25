# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import File, Task, Trash_bin

admin.site.register(File)
admin.site.register(Task)
admin.site.register(Trash_bin)