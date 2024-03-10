from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("r/<int:id>", views.recipe, name="recipe"),
]
