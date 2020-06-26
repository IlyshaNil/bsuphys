from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def templates(request):
    return render(request, "template1.html")
