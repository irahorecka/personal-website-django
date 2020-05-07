from django.urls import path
from . import views

urlpatterns = [
    #  our blog.urls will handle the home (i.e. /blog) and home/about (i.e. /blog/about) urls.
    path('', views.home, name='frontpage-home'),
    path('bikes/', views.bikes, name='frontpage-bikes')
]