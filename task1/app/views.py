from django.shortcuts import render
import csv
import os
from django.conf import settings


def inflation_view(request):
    with open(os.path.join(settings.BASE_DIR, 'inflation_russia.csv'), newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')

    # чтение csv-файла и заполнение контекста
        context = {
            'headers': reader.fieldnames,
            'data': []
        }
        for row in reader:
            values = list(row.values())
            year = values.pop(0)
            summ = values.pop(-1)
            x = lambda x: float(x) if x else ''
            months = [x(i) for i in values]
            context['data'].append({'year': year, 'months': months, 'summ': summ})

    return render(request, 'inflation.html', context)
