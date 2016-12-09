from django.shortcuts import render
from .models import Picture


def gallery(request):
    pictures = Picture.objects.all()
    return render(request, 'gallery.html', {'pictures': pictures})
