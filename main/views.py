from django.shortcuts import render, redirect
from .models import Genre 
from .forms import GenreForm

def index(request):
    return render(request, 'index.html')


def glavna(request):
    return render(request, 'glavnai.html')

def dganry(request):
    genres = Genre.objects.all()
    return render(request, 'dganry.html', {'gen': genres})

def add_gen(request):
    if request.method == "POST":
        genre = GenreForm(request.POST)
        if genre.is_valid():
            genre.save()
        return redirect('/dganry')
    else:
        genreform = GenreForm()
        return render(request, "add_gen.html", {'form': genreform})
    
def edit_genre(request, id_genre):
    g = Genre.objects.get(id=id_genre)

    if request.method == "POST":
        genre = GenreForm(request.POST, instance=g)
        if genre.is_valid():
            genre.save()
        return redirect('/dganry')
    else:
        genreform = GenreForm(instance=g)
        return render(request, "add_gen.html", {'form': genreform})
    
def del_genre(request, id_genre):
    g = Genre.objects.get(id=id_genre)
    g.delete()
    return redirect('/dganry')
    