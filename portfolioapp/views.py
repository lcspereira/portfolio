from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import Project
from datetime import datetime

# Create your views here.
def index(request) -> HttpResponse:
    """List services"""
    services = {
        "Desenvolvimento de software": [
            "Aplicações web responsivas",
            "Aplicações cloud",
            "Aplicações desktop",
            "Frontend",
            "Backend",
            "Integração de sistemas",
            "Scripts de automação",
            "Odoo",
            "Refatoração de código-fonte",
            "Sistemas legados"
        ],
        "Desenvolvimento de websites / e-commerce": [
            "Desenvolvimento e manutenção de websites",
            "Wordpress / WooCommerce",
            "SEO"
        ],
        "Dados": [
            "Banco de dados SQL e NoSQL",
            "Melhoria de performance de banco de dados / queries",
            "Modelagem de dados",
            "Extração e preprocessamento de dados",
            "ETL",
            "Web scraping",
            "Análise e visualização de dados"
        ],
        "Inteligência Artificial / Machine Learning": [
            "Mineração de dados",
            "Data science"
            "Desenvolvimento, treinamento e testes de modelo de IA",
            "Deep learning",
            "Visão computacional"
        ]
    }

    # Convert dictionary items to a list of tuples
    services_list = list(services.items())
    context = {
        "current_year": datetime.now().year,
        'services': services_list
    }
    return render(request, 'index.jinja2', context)

def about(request) -> HttpResponse:
    """About me page"""
    context = {
        "current_year": datetime.now().year
    }
    return render(request, 'under_construction.jinja2', context)

def contact(request) -> HttpResponse:
    """Contact page"""
    context = {
        "current_year": datetime.now().year
    }
    return render(request, 'contact.jinja2', context)

def projects(request) -> HttpResponse:
    """Projects page"""
    projects = Project.objects.all()
    return render(request, 'projects.jinja2', {'projects': projects, "current_year": datetime.now().year})

def project(request, id) -> JsonResponse:
    """Project details endpoint"""
    project = Project.objects.get(id=id)
    return JsonResponse({
        'title_en': project.title_en,
        'title_pt': project.title_pt,
        'description_en': project.description_en,
        'description_pt': project.description_pt,
        'technologies': [technology.name for technology in project.technologies.all()],
        'images': project.images.image.url
    })