from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from taggit.models import Tag


def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        slug=post,
        status="published",
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )
    return render(request, "../templates/templates/post/pageNews.html", {"post": post})


def post_list(request, tag_slug=None):
    object_list = Post.published.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])

    paginator = Paginator(object_list, 3)  # По 3 статьи на каждой странице.
    page = request.GET.get("page")
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:  # Если страница не является целым числом, возвращаем первую страницу.
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(
        request,
        "../templates/templates/post/news.html",
        {"page": page, "posts": posts, "tag": tag},
    )
