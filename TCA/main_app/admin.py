from django.contrib import admin

# Register your models here.
from main_app.models import *


@admin.register(SliderPic)
class AdminSliderPic(admin.ModelAdmin):
    pass


@admin.register(News)
class AdminNews(admin.ModelAdmin):
    pass


@admin.register(Agents)
class AdminAgents(admin.ModelAdmin):
    pass


@admin.register(Images)
class AdminImages(admin.ModelAdmin):
    pass


@admin.register(Table)
class AdminTable(admin.ModelAdmin):
    pass


@admin.register(PermiTable)
class AdminPermiTable(admin.ModelAdmin):
    pass


@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    pass
