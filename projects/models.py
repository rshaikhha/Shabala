# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from time import gmtime, strftime
from django.core.urlresolvers import reverse
# Create your models here.


class Project(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    description = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True,auto_now=False)
    dead_line = models.DateTimeField(auto_now_add=False,auto_now=False)
    public = models.BooleanField(default=True)
    slug = models.SlugField(unique=True)
    
    #tender = models.ManyToManyField(Profile)

    class Meta:
        unique_together = ('title','slug')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("single_project",kwargs={"slug" : self.slug})

    def save(self):
        super(Project, self).save()
        stime = strftime("%H%M%S", gmtime()) 
        self.slug = '%s%s' % (
            self.owner.username, stime
        )    
        super(Project, self).save()

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