from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("t/<str:tag>", views.home, name="home-tag"),
    path("r/<int:id>", views.recipe, name="recipe"),
]
