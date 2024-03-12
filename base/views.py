from django.http import Http404
from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from .data.data import Recipe as R


# Create your views here.
def home(request: WSGIRequest):

    if tag := request.GET.get("tag"):
        recipes = R.filter(lambda x: tag in x.tags or tag in x.creator)
    else:
        recipes = R.all()

    tags = set()
    for recipe in recipes:
        for tag in recipe.tags:
            tags.add(tag)

        if recipe.creator:
            tags.add(recipe.creator)

    context = {"recipes": recipes, "tags": sorted(tags)}
    return render(request, "home.html", context)


def recipe(request: WSGIRequest, id: int):
    try:
        recipe = R.get(id)
    except FileNotFoundError:
        raise Http404()

    context = {"recipe": recipe}

    return render(request, "recipe.html", context)
