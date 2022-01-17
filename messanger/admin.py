from django.contrib import admin

from .models import *


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    pass


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(GlobalMessage)
class GlobalMessageAdmin(admin.ModelAdmin):
    pass
