from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse

from blog.models import Post


def post_list(request: HttpRequest) -> HttpResponse:
    posts = Post.published.all()
    return render(
        request,
        "blog/post/list.html",
        {"posts": posts},
    )


def post_detail(request: HttpRequest, id: int) -> HttpResponse:
    post = get_object_or_404(Post, id=id)
    return render(
        request,
        "blog/post/detail.html",
        {"post": post},
    )
