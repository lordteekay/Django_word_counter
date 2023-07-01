from typing import Dict

from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'index.html')


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
