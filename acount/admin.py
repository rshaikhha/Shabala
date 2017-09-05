# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Profile
# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_time'
    search_fields = []
    list_display = ['__unicode__', 'email', 'email_confirmed', 'date_time', 'update_time']
    list_editable = [ 'email_confirmed',]
    list_filter = []
    readonly_fields = ['date_time','update_time']
    class Meta:
        model = Profile

admin.site.register(Profile,ProfileAdmin)