from django.shortcuts import render, get_object_or_404
from .models import Post, NoteInMedia
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from taggit.models import Tag


def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        status="published",
        publish__year=year,
        publish__month=month,
        publish__day=day,
        slug=post,
    )
    return render(request, "../templates/templates/post/pageNews.html", {"post": post})


def post_list(request, tag_slug=None):
    object_list = Post.published.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])

    paginator = Paginator(object_list, 7)
    page = request.GET.get("page")
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(
        request,
        "../templates/templates/post/news.html",
        {"page": page, "posts": posts, "tag": tag},
    )


def weAreInMedia(request):
    object_list = NoteInMedia.published.all()
    return render(
        request,
        "../templates/templates/post/weAreInMedia.html",
        {"notes": object_list},
    )
