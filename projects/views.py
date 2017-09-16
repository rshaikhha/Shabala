# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Project
from django.http import Http404
# Create your views here.


def project(request, slug):
    try:
        project = Project.objects.get(slug=slug)
        context = {'project': project}
        template = 'project.html'
        return render(request, template, context)
    except:
        raise Http404("This page does not exist!")


def projects(request):
    all = Project.objects.all()
    context = {'projects': all}
    template = 'projects.html'
    return render(request, template, context)