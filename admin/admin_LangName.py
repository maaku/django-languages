#!/usr/bin/env python
# -*- coding: utf-8 -*-

# django-languages: admin/admin_LangName.py
##

from django.contrib import admin
from models import LangName

class LangNameAdmin(admin.ModelAdmin):
    pass

admin.site.register(LangName, LangNameAdmin)

# End of File
##
