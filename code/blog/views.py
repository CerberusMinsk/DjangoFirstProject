from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
    pass
    return HttpResponse('<h1>Пока всё работает</h1>')

def posts_list(request):
    n = ['Oleg', 'Masha', 'Ksusha']
    return render(request, 'blog/index.html', context={'names': n})