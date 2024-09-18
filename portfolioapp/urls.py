from django.urls import path, include
from .views import AboutView, ContactView, IndexView, ProjectsView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('projects/', ProjectsView.as_view(), name='projects'),
    path("summernote/", include("django_summernote.urls"))
]