# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Project,Tender,ProjectFile
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_time'
    search_fields = []
    list_display = ['__unicode__', 'description', 'created_time', 'dead_line']
    list_editable = []
    list_filter = []
    readonly_fields = []
    class Meta:
        model = Project

class TenderAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_time'
    search_fields = []
    list_display = ['__unicode__', 'price', 'description', 'created_time', 'needed_time']
    list_editable = []
    list_filter = []
    readonly_fields = []
    class Meta:
        model = Tender


admin.site.register(Tender,TenderAdmin)
admin.site.register(Project,ProjectAdmin)
admin.site.register(ProjectFile)