# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Topic,Post,Video,File

# Register your models here.

admin.site.register(Topic)
admin.site.register(Post)
admin.site.register(Video)
admin.site.register(File)