#!/usr/bin/env python
# -*- coding: utf-8 -*-

# django-languages: models/model_ExprId.py
##

from django.db import models

from model_ExprTrans import ExprTrans

##
# Note: EVERY model has an implicit AutoField named 'id' which acts as the
#       primary key.  In some cases (ExprId, for example) this field is
#       entirely redundant and never explicitly used, nor is it mentioned in
#       the comments.  However it would be complicated to try to define our
#       own compound primary keys in a portable, safe, extensible, future-
#       proof way (in django).  Additionally, having an AutoField anyway makes
#       it much easier to deal with candidate keys that change value over
#       time, and past experience teaches that one should never assume any
#       meaningful data to remain constant.
##

class ExprId(models.Model):
    """
    A type consisting of values that uniquely represent a linguistic phrase or
    expression.  This is the heart of the django-languages application.  A
    linguistic phrase is identified by a key lookup into the ExprId table.
    Information about expressions, such as translations of the expression into
    human language, is available in other tables.

      Field  Type  Attributes
      =====  ----  ----------
         id  Auto  unique, constant

         Keys: {id}
      Meaning: "There exists a linguistic expression dientified by *id*."

    The question of what, exactly, is a linguistic phrase/expression is left
    up to the developer that uses django-languages.  It could be an individual
    vocabulary word (translated into multiple languages), or an entire article
    for a blog or news site.
    """
    pass

    def __unicode__(self):
        # FIXME: '1' should be replaced with the current locale setting.
        qs = ExprTrans.objects.filter(language='1',
                                      expression=self.id)
        if qs.count() > 0:
          return qs[0].meaning
        return "%d" % self.id

    class Meta(object):
        app_label = "languages"
        verbose_name        = "Expression Identifier"
        verbose_name_plural = "Expression Identifiers"

# End of File
##
