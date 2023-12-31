from django.urls import path

from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.wiki, name="wiki"),
    path("results", views.results, name="results"),
    path("create", views.create, name="create"),
    path("error", views.error, name="error"),
    path("edit/<str:title>", views.edit, name="edit"),
    path("random_page/", views.random_page, name="random_page")
]
