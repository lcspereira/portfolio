from django.contrib import admin
from .models import Image, Technology, Project
from django_summernote.widgets import SummernoteWidget
from django.db import models

# Register your models here.

admin.site.register(Image)
admin.site.register(Technology)


class ProjectAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': SummernoteWidget()},
    }
    fields = ['title_en', 'title_pt', 'description_en', 'description_pt', 'technologies', 'images', 'image_tag']
    readonly_fields = ['image_tag']

admin.site.register(Project, ProjectAdmin)
