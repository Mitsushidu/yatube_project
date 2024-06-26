from django.shortcuts import render, get_object_or_404
from .models import Post, Group
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


def group_posts(request, slug):
    template = 'posts/group_posts.html'
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'posts': posts,
        'group': group,
    }
    return render(request, template, context)
