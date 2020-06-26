from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone

def index(request):
    return render(request, "index.html")


def templates(request):
    posts = Post.objects.latest('publish')
    return render(request, "template1.html", {"posts": posts})
