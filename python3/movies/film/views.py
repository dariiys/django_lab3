from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string


def index(request): # HttpRequest
    t = render_to_string('film/index.html')
    return HttpResponse(t)

def about(request):
    return render(request, 'film/about.html')
def categories(request,comed_id):
    return HttpResponse(f"<h1>Фільми за категоріями</h1> <p>id: {comed_id}</p>")

def categories_by_slug(request, comed_slug):
    return HttpResponse(f"<h1>Фільми за категоріями</h1> <p>slug: {comed_slug}</p>")

def archive(request, year):
    return HttpResponse(f"<h1>Сортування за роками</h1> <p> {year}</p>")