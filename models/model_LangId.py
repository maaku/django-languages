#!/usr/bin/env python
# -*- coding: utf-8 -*-

# django-languages: models/model_LangId.py
##

from django.db import models

from model_LangName import LangName

##
# Note: EVERY model has an implicit AutoField named 'id' which acts as the
#       primary key.  In some cases (LangId, for example) this field is
#       entirely redundant and never explicitly used, nor is it mentioned in
#       the comments.  However it would be complicated to try to define our
#       own compound primary keys in a portable, safe, extensible, future-
#       proof way (in django).  Additionally, having an AutoField anyway makes
#       it much easier to deal with candidate keys that change value over
#       time, and past experience teaches that one should never assume any
#       meaningful data to remain constant.
##

class LangId(models.Model):
    """
    A type consisting of values that uniquely represent a human language.
    Every language is assigned an arbitrary integer value that is used to
    identify it internally, but is typically not visible to users or
    administrators (rather, that language's translated name is used; see the
    LangName class for details).

      Field  Type  Attributes
      =====  ----  ----------
         id  Auto  unique, constant

         Keys: {id}
      Meaning: "There exists a unique human language dientified by *id*."

    The exact definition of "language" is difficult to pin down in a
    linguistic sense, so that decision is left up to the developer (who gets
    to choose which values to fill the database with).  This problem of
    classification mostly arises in the context of spoken language, and as
    consequence there exists accepted standards for classification for the
    common usage case, which is solely concerned with written language.

    FIXME: Defaults should be provided.

    If you're wondering how "language" can be an ambiguous concept, read up on
    the dialects of Chinese, Arabic, and Tibetan, to name a few, or the
    dialects of just about any minority, non-strandardized language.
    """
    ##
    # id is the only field, and it is provided by django automatically
    pass

    def __unicode__(self):
        # FIXME: '1' should be replaced with the current locale setting.
        qs = LangName.objects.filter(source_lang='1',
                                     object_lang=self.id)
        if qs.count() > 0:
          return qs[0].name
        return "%s" % self.id

    class Meta(object):
        app_label = "languages"
        verbose_name        = "Language Identifier"
        verbose_name_plural = "Language Identifiers"

# End of File
##
