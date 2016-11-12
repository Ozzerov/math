from django.shortcuts import render
from .models import Theme, Formula


# Create your views here.


def home(request):
    context = {}
    return render(request, 'home.html', context)


def subjects(request, subject):
    themes = Theme.objects.filter(subject__subject=subject)
    formulas = Formula.objects.filter(theme__subject__subject=subject)

    # themes = Formula.objects.raw("""
    # SELECT theme
    # FROM formulas_formula
    # WHERE subject = '{}'
    # GROUP BY theme
    # ORDER BY avg("order") DESC """.format(subject))
    # a = Formula.objects.raw('SELECT * FROM formulas_formula WHERE subject = {}'.format(subject))
    # for t in themes:
    #     print(t)

    return render(request, 'subjects.html', {'themes': themes, 'formulas': formulas})
