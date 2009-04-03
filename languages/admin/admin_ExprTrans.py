#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# django-languages: admin/admin_ExprTrans.py
##

from django.contrib import admin
from languages.models import ExprTrans

class ExprTransAdmin(admin.ModelAdmin):
    pass

admin.site.register(ExprTrans, ExprTransAdmin)

##
# End of File
##
