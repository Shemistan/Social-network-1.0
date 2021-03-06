from django.shortcuts import render, get_object_or_404
from .models import Post, Group


def index(request):
    selected_posts = Post.objects.order_by("-pub_date")[:10]
    return render(request, "index.html", {"posts": selected_posts})


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.order_by("-pub_date")[:12]
    return render(request, "group.html", {"group": group, "posts": posts})
