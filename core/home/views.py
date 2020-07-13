from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone

def index(request):
    post = Post.published.latest("publish")
    return render(request, "main.html", {"post": post})


def templates(request):
    posts = Post.published.latest("publish")
    return render(request, "template1.html", {"posts": posts})


def dekanat(request):
    return render(request, "dekanat.html")


def spec(request):
    return render(request, "spex.html")