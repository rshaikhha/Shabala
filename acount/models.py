# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic_url = models.URLField()
    date_time = models.DateTimeField(auto_now_add=True,auto_now=False)
    update_time = models.DateTimeField(auto_now_add=False,auto_now=True)
    description = models.TextField()        
    email_confirmed = models.BooleanField(default=False)    
    email = models.EmailField()

    def __unicode__(self):
        return self.user.username

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()