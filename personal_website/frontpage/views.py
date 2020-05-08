from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Post


def home(request):
    title = {
        'title': "Ira Horecka"
    }
    return render(request, 'frontpage/home.html', title)

def bikes(request):
    context = {
        'bikes': Post.objects.all()
    }
    return render(request, 'frontpage/bikes.html', context)

class PostListView(ListView):
    # we need to create a var called model
    model = Post
    template_name = 'frontpage/bikes.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'bikes'  # i.e. posts == context key in our home func
    ordering = ['-date_posted']  # goes oldest to newest -- add a '-' in front to reverse this order
    paginate_by = 3  # no. posts per page
    
class PostDetailView(DetailView):
    model = Post