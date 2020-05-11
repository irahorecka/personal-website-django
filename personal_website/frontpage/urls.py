from django.urls import path
from .views import PostListView, PostDetailView
from . import views

urlpatterns = [
    #  our blog.urls will handle the home (i.e. /blog) and home/about (i.e. /blog/about) urls.
    path('', views.home, name='frontpage-home'),
    path('bikes/', PostListView.as_view(), name='frontpage-bikes'),
    path('bike/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # pk = primary key, int is the type
    path('resume/', views.resume, name="frontpage-resume")
]