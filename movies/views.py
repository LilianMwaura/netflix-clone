from django.shortcuts import  render,redirect
from django.contrib.auth.decorators import login_required
import requests

from netflix.settings import TMDB_API_KEY
from .models import Profile,Image
from .forms import *
from .models import*



# Create your views here.


@login_required(login_url='/accounts/login/')
def homepage(request):
    profiles=   Profile.objects.all()
    return render(request, 'index.html', {'profiles': profiles})


@login_required(login_url='/accounts/login/')
def profile(request,profileId):

    profile = Profile.objects.get(pk = profileId)
    images = Image.objects.filter(id=profile.id).all()

    return render(request,"profile/profile.html",{"profile":profile,"images":images})



@login_required(login_url='/accounts/login/')
def add_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('homepage')

    else:
        form = NewProfileForm()
    return render(request, 'profile/update_profile.html', {"form": form})




@login_required(login_url='Login')
def Recommendations(request):
    now_playing_movies_request = requests.get("https://api.themoviedb.org/3/movie/now_playing?api_key=aabb0c7ca8b510be8e9e03a4e8ffd9aa")
    now_playing_movies_results = now_playing_movies_request.json()
    now_playing_movies = now_playing_movies_results['results']

    top_rated_shows_request = requests.get("https://api.themoviedb.org/3/tv/top_rated?api_key=aabb0c7ca8b510be8e9e03a4e8ffd9aa")
    top_rated_shows_results = top_rated_shows_request.json()
    top_rated_shows = top_rated_shows_results['results']

    top_rated_request = requests.get("https://api.themoviedb.org/3/movie/top_rated?api_key=aabb0c7ca8b510be8e9e03a4e8ffd9aa")
    top_rated_results = top_rated_request.json()
    top_rated = top_rated_results['results']

    popular_tv_request = requests.get("https://api.themoviedb.org/3/tv/popular?api_key=aabb0c7ca8b510be8e9e03a4e8ffd9aa" )
    popular_tv_results = popular_tv_request.json()
    popular_tv = popular_tv_results['results']

    upcoming_request = requests.get("https://api.themoviedb.org/3/movie/upcoming?api_key=aabb0c7ca8b510be8e9e03a4e8ffd9aa" )
    upcoming_results = upcoming_request.json()
    upcoming = upcoming_results['results']

    return render(request, 'Recommendations.html', {'now_playing_movies':now_playing_movies, 'top_rated_shows':top_rated_shows, 'top_rated':top_rated, 'upcoming':upcoming, 'popular_tv':popular_tv})



@login_required(login_url='Login')
def MovieDetails(request, movie_id):
    movie_details_request = requests.get("https://api.themoviedb.org/3/movie/" + str(movie_id) + "?api_key=" + TMDB_API_KEY)
    movie_details_results = movie_details_request.json()
    movie_details = movie_details_results

    movie_video_request = requests.get("https://api.themoviedb.org/3/movie/" + str(movie_id) + "/videos?api_key=" + TMDB_API_KEY)
    movie_video_results = movie_video_request.json()
    movie_videos = movie_video_results['results']
    newDict = dict()
    for movie in movie_videos:
        if movie['type'] == 'Trailer':
            newDict['key'] = movie['key']

    return render(request, 'Movie Details.html', {'movie_details':movie_details, 'movie_id':movie_id, 'newDict':newDict})