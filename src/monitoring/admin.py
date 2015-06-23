
from  __future__ import absolute_import
from django.contrib import admin
from .models import Url, CheckResult


@admin.register(Url)
class UrlAdmin(admin.ModelAdmin):
    list_display = ('url', 'last_code')


@admin.register(CheckResult)
class CheckResultAdmin(admin.ModelAdmin):
    pass


