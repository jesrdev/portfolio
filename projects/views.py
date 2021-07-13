from django import template
from django.shortcuts import render, get_object_or_404
from .models import Project
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def homepage(request):
    projects = Project.objects
    template = loader.get_template('projects/home.html')
    return HttpResponse(template.render({'projects':projects}, request))


def detail(request, project_id):
    project_detail = get_object_or_404(Project, pk=project_id)
    template = loader.get_template('projects/detail.html')
    return HttpResponse(template.render({'project':project_detail}, request))