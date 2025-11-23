from django.urls import path
from . import views
from .views import download_mp3
#from .views import fetch_info, download

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('album/', views.album, name='album'),
    path('play/', views.play, name='play'),
    path('download/', views.download, name='download'),
    path("download-mp3/", download_mp3, name="download_mp3"),

    
    ]


#path("download-mp3/", download_mp3, name="download_mp3"),
