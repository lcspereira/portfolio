from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import Project
from datetime import datetime

# Create your views here.
def index(request) -> HttpResponse:
    context = {
        "current_year": datetime.now().year
    }
    return render(request, 'index.jinja2', context)

def about(request) -> HttpResponse:
    context = {
        "current_year": datetime.now().year
    }
    return render(request, 'about.jinja2', context)

def contact(request) -> HttpResponse:
    context = {
        "current_year": datetime.now().year
    }
    return render(request, 'contact.jinja2', context)

def projects(request) -> HttpResponse:
    projects = Project.objects.all()
    return render(request, 'projects.jinja2', {'projects': projects, "current_year": datetime.now().year})

def project(request, id) -> JsonResponse:
    project = Project.objects.get(id=id)
    return JsonResponse({
        'title_en': project.title_en,
        'title_pt': project.title_pt,
        'description_en': project.description_en,
        'description_pt': project.description_pt,
        'technologies': [technology.name for technology in project.technologies.all()],
        'images': project.images.image.url
    })