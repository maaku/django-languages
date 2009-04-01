#!/usr/bin/env python
# -*- coding: utf-8 -*-

# django-languages: admin/admin_ExprId.py
##

from django.contrib import admin
from languages.models import ExprId

class ExprIdAdmin(admin.ModelAdmin):
    pass

admin.site.register(ExprId, ExprIdAdmin)

# End of File
##
