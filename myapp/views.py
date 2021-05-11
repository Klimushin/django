from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return HttpResponse("Home page")


def article_main(request):
    return HttpResponse("Main article")


def article_number(request, article_id):
    return HttpResponse("Article number {}".format(article_id))


def article_number_archive(request, article_id):
    return HttpResponse("http://127.0.0.1:8000/article/{}/archive".format(article_id))


def article_number_slug(request, article_id, slug_text):
    return HttpResponse("http://127.0.0.1:8000/article/{}/{}".format(article_id, slug_text))


def article(request, article_id, title):
    return HttpResponse("Article {} with {}".format(article_id, title))


def articles(request):
    return HttpResponse("http://127.0.0.1:8000/acricles")


def articles_archive(request):
    return HttpResponse("http://127.0.0.1:8000/acrticles/archive")


def users(request):
    return HttpResponse("http://127.0.0.1:8000/users")


def users_number(request, users_id):
    return HttpResponse("Users number {}".format(users_id))


