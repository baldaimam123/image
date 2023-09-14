from django.shortcuts import render
from .models import Post

# Create your views here.


def index(request):
    posts = Post.objects.all()
    categories = Post.objects.values("category").distinct()

    context = {
        "judul": "Selamat Datang di BLOGKU",
        "Posts": posts,
        "Categories": categories,
    }
    return render(request, "blog/index.html", context)


def detailPost(request, slugInput):
    posts = Post.objects.get(slug=slugInput)
    categories = Post.objects.values("category").distinct()
    context = {
        "judul": "Selamat Datang di BLOGKU",
        "Posts": posts,
        "Categories": categories,
    }
    return render(request, "blog/detail.html", context)


def categoryPost(request, categoryInput):
    posts = Post.objects.filter(category=categoryInput)
    categories = Post.objects.values("category").distinct()
    context = {
        "judul": "Selamat Datang di BLOGKU",
        "Posts": posts,
        "Categories": categories,
    }
    return render(request, "blog/category.html", context)


def gambarPost(request, gambarInput):
    posts = Post.objects.filter(foto=gambarInput)

    context = {
        "judul": "Selamat Datang di BLOGKU",
        "Posts": posts,
    }
    return render(request, "blog/index.html", context)
