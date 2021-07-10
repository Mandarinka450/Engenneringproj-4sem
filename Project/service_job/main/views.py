from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Vacancies, Reviews, Reviews_about_service
from .forms import ReviewForm
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)


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

def index3(request):
    reviews = Reviews_about_service.objects.all()
    count2 = Reviews_about_service.objects.all().count()
    paginator = Paginator(reviews, 6)  # 6 поста на каждой странице
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
        'count2': count2,
    }
    return render(request, 'main/reviews.html', context=context)


def index4(request):
    return render(request, 'main/adreview.html')

def create_view(request):
    context ={}

    form = ReviewForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

        form.save()
        return HttpResponseRedirect("/reviews")

    context['form']= form
    return render(request, "main/adreview.html", context)

def update_view(request, id_review):
    context ={}

    obj = get_object_or_404(Reviews_about_service, id_review=id_review)

    form = ReviewForm(request.POST or None, instance=obj)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        form.save()
        return HttpResponseRedirect("/reviews")

    # add form dictionary to context
    context["form"] = form

    return render(request, "main/update_review.html", context)

def delete_view(request, id_review):
    # dictionary for initial data with
    # field names as keys
    context ={}

    # fetch the object related to passed id
    obj = get_object_or_404(Reviews_about_service, id_review=id_review)


    if request.method =="POST":

        obj.delete()
        return HttpResponseRedirect("/reviews")

    return render(request, "main/delete_review.html", context)
