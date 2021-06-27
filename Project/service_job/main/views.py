from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Vacancies


def index(request):
    return render(request, 'main/index.html')

def index2(request):
    search_query = request.GET.get('search', '')
    if search_query:
        vacancies = Vacancies.objects.filter(name_of_vacancy__icontains=search_query)
    else:
        vacancies = Vacancies.objects.all()
    count = Vacancies.objects.all().count()

    paginator = Paginator(vacancies, 4)  # 4 поста на каждой странице
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    is_paginated = page.has_other_pages()
    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''
    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''
    context = {
        'page_object': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url,
        'count': count,
    }

    return render(request, 'main/vacancies.html', context=context)
