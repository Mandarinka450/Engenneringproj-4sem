from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Vacancies


def index(request):
    return render(request, 'main/index.html')

def index2(request):
    vacancies = Vacancies.objects.all()
    paginator = Paginator(vacancies, 4)  # 4 поста на каждой странице
    page = request.GET.get('page')
    try:
        page = paginator.page(page)
    except PageNotAnInteger:
        # Если страница не является целым числом, поставим первую страницу
        page = paginator.page(1)
    except EmptyPage:
        # Если страница больше максимальной, доставить последнюю страницу результатов
        page = paginator.page(paginator.num_pages)
    return render(request, 'main/vacancies.html', {'vacancies': vacancies, 'page': page})
