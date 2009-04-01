#!/usr/bin/env python
# -*- coding: utf-8 -*-

# django-languages: admin/admin_LangId.py
##

from django.contrib import admin
from models import LangId

class LangIdAdmin(admin.ModelAdmin):
    pass

admin.site.register(LangId, LangIdAdmin)

# End of File
##
