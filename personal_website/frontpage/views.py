import json
from django.shortcuts import render, get_object_or_404
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic import ListView, DetailView

from .models import Post


def home(request):
    return render(request, 'frontpage/home.html')

def resume(request):
    with open(staticfiles_storage.path('resume.json')) as resume_content:
        context = json.load(resume_content) 
        return render(request, 'frontpage/resume.html', context)


class PostListView(ListView):
    # we need to create a var called model
    model = Post
    template_name = 'frontpage/bikes.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'bikes'  # i.e. posts == context key in our home func
    ordering = ['-date_posted']  # goes oldest to newest -- add a '-' in front to reverse this order
    paginate_by = 1  # no. posts per page
    
class PostDetailView(DetailView):
    model = Post