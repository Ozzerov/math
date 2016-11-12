from django.shortcuts import render
from .models import Theme


def home(request):
    context = {}
    return render(request, 'home.html', context)


def subjects(request, subject):
    themes = Theme.objects.filter(subject__subject=subject)
    return render(request, 'subjects.html', {'themes': themes})
