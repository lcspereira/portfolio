from django.db import models
from django.utils.html import mark_safe
from django.conf import settings

# Create your models here.

class Image(models.Model):
    image = models.ImageField(upload_to=f"{settings.STATIC_ROOT}/img")

    def __str__(self):
        return self.image.url

class Technology(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Project(models.Model):
    title_en = models.CharField(max_length=100)
    title_pt = models.CharField(max_length=100)
    description_en = models.TextField()
    description_pt = models.TextField()
    technologies = models.ManyToManyField(Technology)
    images = models.ManyToManyField(Image)

    def __str__(self):
        return self.title_en
    
    def image_tag(self) -> str:
        """
        Generate project's thumbnail HTML tag

        Returns:
            str: HTML tag
        """
        if self.images is not None and self.images.count() > 0:
            return mark_safe('<img src="%s" width="150" height="150" />' % (self.images.first().image.url))
        return 'No image'