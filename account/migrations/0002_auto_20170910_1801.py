# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-10 18:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='profile_pic_url',
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default=1, upload_to='profiles/images/'),
            preserve_default=False,
        ),
    ]