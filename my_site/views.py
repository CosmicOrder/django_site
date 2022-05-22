from django.shortcuts import render


def index(request):
    return render(request, 'my_site/index.html')


def reverse_engineering(request):
    return render(request, 'my_site/reverse-engineering.html',
                  {'page_name': '-reverse-engineering'})


def drafts(request):
    return render(request, 'my_site/drafts.html', {'page_name': '-drafts'})


def visualize(request):
    return render(request, 'my_site/visualize.html', {'page_name': '-visualize'})


def projects(request):
    return render(request, 'my_site/projects.html')
