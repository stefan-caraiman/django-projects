from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Album
# Create your views here.

def index(request):
    all_albums = Album.objects.all()
    context_data = {
        'all_albums': all_albums,
    }
    return render(request, 'music/index.html', context_data)

def detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, "music/detail.html", {'album': album})

# Vid nr 22
