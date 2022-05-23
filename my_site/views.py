from django.shortcuts import render

from my_site.site_content import main_page_content


def index(request):
    return render(request, 'my_site/index.html', main_page_content)


def reverse_engineering(request):
    return render(request, 'my_site/reverse-engineering.html',
                  {
                      'page_name': '-reverse-engineering',
                      'title': 'Реверсивный инжениринг'
                  })


def drafts(request):
    return render(request, 'my_site/drafts.html',
                  {
                      'page_name': '-drafts',
                      'title': 'Разработка КД'

                  })


def visualize(request):
    return render(request, 'my_site/visualize.html',
                  {
                      'page_name': '-visualize',
                      'title': '3д моделирование'
                  })


def projects(request):
    return render(request, 'my_site/projects.html')
