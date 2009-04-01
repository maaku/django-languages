#!/usr/bin/env python
# -*- coding: utf-8 -*-

# django-languages: model_ExprTrans.py
##

from django.db import models

class ExprTrans(models.Model):
    """
    The ExprTrans table contains translations of expression objects into
    various languages.

            Field    Type  Attributes
            =====    ----  ----------
         language  LangId
       expression  ExprId
          meaning  String
          reading  String

         Keys: {language, expression}
      Meaning: "The linguistic unit identified by *expression* is written
                *meaning* in the language identified by *language*, and
                pronounced according to the phonetic transcription *reading*."

    An ExprId object is an abstract, language-neutral representation of a
    linguistic phrase.  Entries in the ExprTrans table make an ExprId object
    concrete and real by providing a translation of that phrase into an actual
    human language.  *expression* and *language* identify the phrase of
    interest and the language of translation, respectfully.  *expression* is
    always expressed in standard written form, while *reading* provide a
    phonetic transcription.  No standard exists for *reading*, as methods for
    phonetic transcription vary from language to language.
    """
    # language of translation
    # e.g, id:2 # for Japanese
    language   = models.ForeignKey('LangId')
    # expression id
    # e.g, id:1234 # for "He is a foreigner, too."
    expression = models.ForeignKey('ExprId')
    # translated into language
    # e.g, "彼も外国人だ。"
    meaning    = models.TextField()
    # translation written phonetically
    # e.g, "かれ も がいこくじん だ。"
    reading    = models.TextField(blank=True)

    def __unicode__(self):
        return "".join(["(Expression:%s in Language:%s) -> (%s, %s)" %
                        (self.expression,
                         self.language,
                         self.meaning,
                         self.reading)])

    class Meta(object):
        unique_together = (('language'), ('expression'))
        verbose_name        = "Localized Expression"
        verbose_name_plural = "Localized Expressions"

# End of File
##
