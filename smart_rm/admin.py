# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *

admin.site.register(Log)
admin.site.register(Task)
admin.site.register(Trash_bin)
admin.site.register(RegularTask)
admin.site.register(History)
