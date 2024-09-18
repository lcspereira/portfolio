from typing import Any
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.generic import TemplateView, ListView, DetailView
from .models import Project
from datetime import datetime

class BasePortfolioMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_year'] = datetime.now().year
        
        # SEO
        context['description'] = 'Lucas Pereira - Engenheiro de software freelancer - Desenvolvimento de software, websites, e-commerce, dados, inteligência artificial e machine learning.'
        keywords = [
            'desenvolvimento de software', 'software development',
            'freelancer',
            'engenharia de software', 'software engineering',
            'engenheiro de software', 'software engineer',
            'websites',
            'e-commerce',
            'dados', 'data',
            'inteligência artificial', 'artificial intelligence',
            'machine learning', 
            'python',
            'django',
            'javascript',
            'vue',
            'sql',
            'nosql',
            'odoo',
            'wordpress',
            'woocommerce',
            'seo',
            'web scraping',
            'data science',
            'deep learning',
            'visão computacional', 'computer vision'
        ]
        context['keywords'] = ', '.join(keywords)
        return context
    
class IndexView(BasePortfolioMixin, TemplateView):
    template_name = 'index.jinja2'
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = self.services.items()
        return context

class AboutView(BasePortfolioMixin, TemplateView):
    template_name = 'under_construction.jinja2'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class ContactView(BasePortfolioMixin, TemplateView):
    template_name = 'contact.jinja2'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class ProjectsView(BasePortfolioMixin, ListView):
    template_name = 'projects.jinja2'
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        projects = Project.objects.all()
        context['projects'] = projects
        return context

class ProjectView(BasePortfolioMixin, DetailView):
    model = Project

    def render_to_response(self, context: dict[str, Any], **response_kwargs: Any) -> HttpResponse:
        project = self.get_object()
        data = {
            'title_en': project.title_en,
            'title_pt': project.title_pt,
            'description_en': project.description_en,
            'description_pt': project.description_pt,
            'technologies': [technology.name for technology in project.technologies.all()],
            'images': project.images.image.url
        }
        return JsonResponse(data)
    
