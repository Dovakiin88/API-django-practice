from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Movie

# Create your views here.
# NOTE: view function could be HTML/CSS, XML ETC

def mainpage (request):
    movies= Movie.objects.all()
    #NOTE: this woudl return a list of itemsoutput= [', '.join([m.title for m in movies])]
    #NOTE: to create a filter statement, 
    #Movie.objects.filter(release_year=2010)
    #NOTE: to get a single object, Movie.objects.get(id=1)
    #return HttpResponse(output)
    return render(request, 'movies/index.html', {'movies': movies})

def detail(request, movie_id):
        movie= get_object_or_404(Movie, pk=movie_id)
        return render(request, 'movies/detail.html', { 'movie': movie })
    
'''
If you end up having issues try pip install pylint-django.
then create a file in root of project, ie same level as movies and vidly
create a new file called: .pylintrc.
This is a configuration file for pylint
In that file type:
    load-plugins=pylint-django
'''