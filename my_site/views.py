from django.shortcuts import render

from my_site.models import Sample
from my_site.site_content import main_page_content


def index(request):
    return render(request, 'my_site/index.html', main_page_content)


def reverse_engineering(request):
    context = {
        'page_name': '-reverse-engineering',
        'title': 'Реверсивный инжениринг',
    }
    return render(request, 'my_site/reverse-engineering.html', context)


def drafts(request):
    context = {
        'page_name': '-drafts',
        'title': 'Разработка КД',
    }
    return render(request, 'my_site/drafts.html', context)


def visualize(request):
    context = {
        'page_name': '-visualize',
        'title': '3д моделирование',
    }
    return render(request, 'my_site/visualize.html', context)


def projects(request):
    samples = Sample.objects.all()
    portfolio = {}
    for sample in samples:
        portfolio.setdefault(sample.category, []).append(sample)

    context = {
        'page_name': '-projects',
        'title': 'Портфолио',
        'portfolio': portfolio,
    }

    return render(request, 'my_site/projects.html', context)
