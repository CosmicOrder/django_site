from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='main_page'),
    path('reverse_engineering/', reverse_engineering,
         name='reverse_engineering'),
    path('drafts/', drafts, name='drafts'),
    path('visualize/', visualize, name='visualize'),
    path('projects/', projects, name='projects'),
]
