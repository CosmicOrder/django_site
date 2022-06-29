from django.conf.urls.static import static
from django.urls import path

from reverse_engineering_site import settings
from . import views

urlpatterns = [
    path('', views.index, name='main_page'),
    path(
        'reverse_engineering/',
        views.reverse_engineering,
        name='reverse_engineering',
    ),
    path('drafts/', views.drafts, name='drafts'),
    path('visualize/', views.visualize, name='visualize'),
    path('projects/', views.projects, name='projects'),
    path('form', views.form_processing, name='form'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
