from django.shortcuts import render
from django.http import HttpResponse
from .models import Album
# Create your views here.

def index(request):
    all_albums = Album.objects.all()
    html = ""
    for album in all_albums:
        url = "/music/%s/" % album.id
        title = album.album_title
        html += "<a href='%s'> %s </a><br>" % (url, title)
    return HttpResponse(html)

def detail(request, album_id):
    return HttpResponse("<h2>Details for Album: %s</h2>" % album_id)
