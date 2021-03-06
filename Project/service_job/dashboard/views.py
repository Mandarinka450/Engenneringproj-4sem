from django.http import JsonResponse
from django.shortcuts import render
from django.core import serializers
from .models import Category


def dashboard_with_pivot(request):
    return render(request, 'dashboard_with_pivot.html', {})

def pivot_data(request):
    dataset = Category.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)
