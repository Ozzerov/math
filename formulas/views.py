from django.shortcuts import render
from .models import Subject, Theme


def home(request):
    context = {}
    return render(request, 'home.html', context)


def subjects(request, subject):
    s = Subject.objects.get(pk=subject)
    themes = Theme.objects.filter(subject__pk=subject)

    return render(request, 'subjects.html', {'subject': s, 'themes': themes})
