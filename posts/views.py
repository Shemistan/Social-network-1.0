from django.shortcuts import render, get_object_or_404
from .models import Post, Group


def index(request):
    selected_posts = Post.objects.all()[:11]
    return render(request, "index.html", {"posts": selected_posts})


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:12]
    return render(request, "group.html", {"group": group, "posts": posts})
