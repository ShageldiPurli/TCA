from modeltranslation import translator
from modeltranslation.translator import TranslationOptions, register

from main_app import models
from main_app.models import SliderPic


@translator.register(models.SliderPic)
class SliderDescriptionOption(translator.TranslationOptions):
    fields = ('description',)


@translator.register(models.News)
class NewsTranlaterOption(translator.TranslationOptions):
    fields = ('name', 'text',)


@translator.register(models.Agents)
class AgentsTranslaterOption(translator.TranslationOptions):
    fields = ('name', 'description',)


@translator.register(models.Table)
class TableTranslatorOption(translator.TranslationOptions):
    fields = ('name', 'table',)


@translator.register(models.PermiTable)
class PermiTableTranslater(translator.TranslationOptions):
    fields = ('mintable',)
