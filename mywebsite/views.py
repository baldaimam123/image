from django.shortcuts import render


def index(request):
    context = {
        "judul": "Selamat Datang",
    }
    return render(request, "index.html", context)
