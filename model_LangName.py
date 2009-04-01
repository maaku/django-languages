#!/usr/bin/env python
# -*- coding: utf-8 -*-

# django-languages: model_LangName.py
##

from django.db import models

class LangName(models.Model):
    """
    The LangName table enables the mapping of LangId identifiers to language-
    specific Unicode strings.

            Field    Type  Attributes
            =====    ----  ----------
      source_lang  LangId
      object_lang  LangId
             name  String

         Keys: {source_lang, object_lang}
               {source_lang, name}
      Meaning: "The language identified by *object_lang* is written *name* in
                the language identified by *source_lang*."

    As much as possible, the interaction by users and administrators with data
    of the LangId type should be through the native-language mappings of
    LangName.  For example, a widget that is often used is a pull-down menu
    that contains all the supported languages for some task or feature.
    Internally, the list of supported languages is of type LangId, but these
    meaningless numbers should be mapped into the user or administrator's
    native language before being passed to user interface code, and mapped
    back to LangId when a selection is made.  For this reason there exists a
    requirement that language names be unique within any given language in
    order to avoid confusion and to enable the reverse mapping.
    """
    # e.g, id:2 # for Japanese
    source_lang = models.ForeignKey('LangId')
    # e.g, id:1 # for English
    object_lang = models.ForeignKey('LangId', related_name='translated_into')
    # e.g, "英語"
    name = models.TextField()

    def __unicode__(self):
        return "".join(["(",
                        unicode(self.source_lang),
                        ", ",
                        unicode(self.object_lang),
                        ") -> \"",
                        self.name,
                        "\""])

    class Meta(object):
        unique_together     = (("source_lang", "object_lang"),
                               ("source_lang", "name"))
        verbose_name        = "Localized Language Name"
        verbose_name_plural = "Localized Language Names"

# End of File
##
