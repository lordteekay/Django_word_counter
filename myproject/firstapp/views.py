from typing import Dict

from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.
def index(request):
    context = {
        'name': 'Tokunbo',
        'age': 23,
        'nationality': 'Nigeria'
    }
    return render(request, 'index.html', context)


def counter(request):
    text = request.POST['text']
    if len(text) == 0:
        return render(request, 'block.html')
    else:
        count = {
            'words': len(text.split()),
            'characters': len(text)
        }
        return render(request, 'counter.html', count)
