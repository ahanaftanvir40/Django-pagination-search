from django.shortcuts import render
from .models import Movies
from django.views.generic.list import ListView
from django.core.paginator import Paginator
# Create your views here.

#class IndexClassView(ListView):
    #model = Movies
    #template_name = 'movie/movie_list.html'
    #context_object_name = 'movie_objects'
    #paginate_by = 2

def movie_list(request):
    movie_objects = Movies.objects.all()

    context = {
        'movie_objects' : movie_objects
    }

    movie_name = request.GET.get('movie_name')

    if movie_name != '' and movie_name is not None:
        movie_objects = movie_objects.filter(name__icontains = movie_name) #icontains relaxes the search and show the all possibility


    paginator = Paginator(movie_objects, 3)
    page = request.GET.get('page')
    movie_objects =paginator.get_page(page) #if we name the var something else then
                                            #we need to pass that as a context

    return render(request, 'movie/movie_list.html',{'movie_objects': movie_objects}) # we must pass the paginator as context
