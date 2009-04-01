#!/usr/bin/env python
# -*- coding: utf-8 -*-

# django-languages: admin.py
##

from django.contrib import admin

from model_ExprId    import ExprId
from admin_ExprId    import ExprIdAdmin
from model_ExprTrans import ExprTrans
from admin_ExprTrans import ExprTransAdmin
from model_LangId    import LangId
from admin_LangId    import LangIdAdmin
from model_LangName  import LangName
from admin_LangName  import LangNameAdmin

admin.site.register(ExprId,       ExprIdAdmin)
admin.site.register(ExprTrans, ExprTransAdmin)
admin.site.register(LangId,       LangIdAdmin)
admin.site.register(LangName,   LangNameAdmin)

# End of File
##
