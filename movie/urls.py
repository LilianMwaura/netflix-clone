from django.urls import path,re_path
from . import views

urlpatterns = [
    path('popular', views.popular, name='popular'),
    path('upcoming', views.upcoming, name='upcoming'),
    path('trending', views.trending, name='trending'),
    # re_path(r'movie/(?P<movie_id>[\d+])', views.movie, name='movie')
]