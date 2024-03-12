from django.http import Http404
from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from .data.data import Recipe as R


# Create your views here.
def home(request: WSGIRequest, tag=None):

    if tag:
        recipes = R.filter(lambda x: tag in x.tags or tag in x.creator)
    else:
        recipes = R.all()

    tags = set()
    creators = dict()
    for recipe in recipes:
        for tag in recipe.tags:
            tags.add(tag)

        if recipe.creator in creators and recipe.creator:
            creators[recipe.creator] += 1
        else:
            creators[recipe.creator] = 1

    for creator, instances in creators.items():
        if instances > 1:
            tags.add(creator)

    context = {"recipes": sorted(recipes, key=lambda x: x.id), "tags": sorted(tags)}
    return render(request, "home.html", context)


def recipe(request: WSGIRequest, id: int):
    try:
        recipe = R.get(id)
    except FileNotFoundError:
        raise Http404()

    context = {"recipe": recipe}

    return render(request, "recipe.html", context)
