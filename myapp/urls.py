from django.urls import path

from myapp.views import *

urlpatterns = [
    path("home/", home),
    path("article/", article_main),
    path("article/<int:article_id>/", article_number),
    path("article/<int:article_id>/archive/", article_number_archive),
    path("article/<int:article_id>/<slug:slug_text>/", article_number_slug),
    path("article/<int:article_id>/<str:title>/", article),
    path("articles/", articles),
    path("articles/archive/", articles_archive),
    path("users/", users),
    path("users/<int:users_id>/", users_number),


]
