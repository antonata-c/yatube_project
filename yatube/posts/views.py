from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {
        'text': 'Это главная страница проекта Yatube',
    }
    template = 'posts/index.html'
    return render(request, template, context)


def group_posts(request, slug):
    context = {
        'text': 'Здесь будет информация о группах проекта Yatube',
    }
    template = 'posts/group_list.html'
    return render(request, template, context)

