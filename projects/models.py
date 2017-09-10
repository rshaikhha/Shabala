# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Project(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    description = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True,auto_now=False)
    dead_line = models.DateTimeField(auto_now_add=False,auto_now=False)
    public = models.BooleanField(default=True)
    #tender = models.ManyToManyField(Profile)

    def __unicode__(self):
        return self.title

class ProjectFile(models.Model):
    project = models.ForeignKey(Project)
    file = models.FileField(upload_to='projects/images/')

    def __unicode__(self):
        return self.project.title

class Tender(models.Model):
    tender = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    price = models.BigIntegerField()
    description = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True,auto_now=False)
    needed_time = models.DateTimeField(auto_now_add=False,auto_now=False)

    def __unicode__(self):
        return self.tender.username 