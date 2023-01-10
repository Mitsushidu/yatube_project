from django.shortcuts import render
from .models import Post
# Create your views here.


def index(request):
    template = 'posts/index.html'
    description = 'Это главная страница проекта Yatube'
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'description': description,
        'posts': posts,
    }
    return render(request, template, context)


def group_list(request):
    template = 'posts/group_list.html'
    description = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'description': description,
    }
    return render(request, template, context)
