import os

import pandas as pd
from django.shortcuts import render

from my_site.site_content import main_page_content

samples_path = os.getenv('SAMPLES_PATH', default='samples.xlsx')

samples_from_excel_df = pd.read_excel(samples_path, keep_default_na=False)
samples_from_excel = samples_from_excel_df.to_dict(orient='records')

portfolio = {}
for samples_from_excel in samples_from_excel:
    portfolio.setdefault(samples_from_excel['Category'], []) \
        .append(samples_from_excel)


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


data = {'page_name': '-projects', 'title': 'Портфолио', 'portfolio': portfolio}


def projects(request):
    return render(request, 'my_site/projects.html', data)
