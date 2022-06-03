import os
import requests
from django.shortcuts import render
api_key=os.environ.get('API_KEY')

# Create your views here.

def popular(request):
    url = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}'
    response = requests.get(url)
    data = response.json()
    
    
    context = {
        'data': data
    }
    return render(request, 'movie/popular.html', context)

def upcoming(request):
    url = f'https://api.themoviedb.org/3/movie/upcoming?api_key={api_key}'
    response = requests.get(url)
    data = response.json()
    
    
    context = {
        'data': data
    }
    return render(request, 'movie/upcoming.html', context)

def trending(request):
    url = f'https://api.themoviedb.org/3/movie/now_playing?api_key={api_key}'
    response = requests.get(url)
    data = response.json()
    
    
    context = {
        'data': data
    }
    return render(request, 'movie/trending.html', context)

def view_movies(request):
    data = requests.get(f"https://api.themoviedb.org/3/movie/297802?api_key={api_key}&language=en-US")
    recommendations = requests.get(f"https://api.themoviedb.org/3/movie/297802/recommendations?api_key={api_key}&language=en-US")
    return render(request, "movies.html", {
        "data": data.json(),
        "recommendations": recommendations.json(),
        "type": "movie",
    })

# def movie(request, movie_id):
#     url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}'
    
#     response = requests.get(url)
#     data = response.json()

#     movie = data['id']
#     context={
#         'movie':movie
#     }
    
#     return render(request, 'movie/movie-detail.html',context)