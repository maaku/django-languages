#!/usr/bin/env python
# -*- coding: utf-8 -*-

# django-languages: models/__init__.py
##

##
# Note: EVERY model has an implicit AutoField named 'id' which acts as the
#       primary key.  In some cases (LangName, for example) this field is
#       entirely redundant and never explicitly used, nor is it mentioned in
#       the comments.  However it would be complicated to try to define our
#       own compound primary keys in a portable, safe, extensible, future-
#       proof way (in django).  Additionally, having an AutoField anyway makes
#       it much easier to deal with candidate keys that change value over
#       time, and past experience teaches that one should never assume any
#       meaningful data to remain constant.
##

from django.db import models

from model_ExprId    import *
from model_ExprTrans import *
from model_LangId    import *
from model_LangName  import *

# End of File
##
