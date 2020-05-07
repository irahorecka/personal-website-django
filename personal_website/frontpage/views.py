from django.shortcuts import render
from .models import Post

posts = [
    {
        "bike_make": 'GT',
        "bike_make_url": 'https://en.wikipedia.org/wiki/GT_Bicycles',
        "bike_model": '2001 GT Attack',
        "content": 'First post content'
    },
    {
        "bike_make": 'Schwinn',
        "bike_make_url": 'https://en.wikipedia.org/wiki/Schwinn_Bicycle_Company',
        "bike_model": '1983 Schwinn Traveler',
        "content": 'Second post content'
    }
]


def home(request):
    title = {
        'title': "Home Page"
    }
    return render(request, 'frontpage/home.html', title)

def bikes(request):
    context = {
        'bikes': Post.objects.all()
    }
    return render(request, 'frontpage/bikes.html', context)
    