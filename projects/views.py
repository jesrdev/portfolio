from django.forms.fields import NullBooleanField
from django.shortcuts import render, get_object_or_404
from .models import Project
from django.forms import ModelForm

class PhotoForm(ModelForm):
    class Meta:
        model = Project

# Create your views here.
def homepage(request):
    context = NullBooleanField
    projects = Project.objects
    return render(request, 'projects/home.html', {'projects':projects}) 

def detail(request, project_id):
    context = NullBooleanField
    project_detail = get_object_or_404(Project, pk=project_id)
    return render(request, 'projects/detail.html', {'project':project_detail})