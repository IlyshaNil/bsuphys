from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone
from django.utils.translation import LANGUAGE_SESSION_KEY
from django.conf import settings
from django.http import HttpResponse
from django.utils import translation

def language_switch_en():
    user_language = 'en'
    translation.activate(user_language)
    response = HttpResponse()
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)
    return(response)


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


def abitur(request):
    return render(request, "enrollee.html")


def info(request):
    return render(request, "mainInf.html")


def faculty(request):
    return render(request, "1.html")


def enter(request):
    return render(request, "2.html")


def cooperation(request):
    return render(request, "3.html")


def science(request):
    return render(request, "4.html")


def education(request):
    return render(request, "5.html")


def contacts(request):
    return render(request, "6.html")