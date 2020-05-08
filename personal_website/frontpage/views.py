from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Post


def home(request):
    context = {
        'title': "Ira Horecka",
        'work_experience': [
            {
                "company": "Five Prime Therapeutics",
                "position": "Research Associate II",
                "date": "Dec. 2017 – Sept. 2019",
                "body": [
                    "Implemented Golden Gate cloning for high-throughput recombinant protein and antibody synthesis.",
                    """Pioneered a transient transfection protocol for rapidly evaluating protein expression and established a
                    technique that boosts expression and uses 50% or less DNA than required in standard protocols.""",
                    """Served as the molecular biology lead in developing automated DNA dilution workflows and organizing
                    collaborative projects with the systems engineering department.""",
                    "Developed automation scripts on TECAN, Biomek, Qpix and served as the power user to train others.",
                    "Scripted automated tasks using Python and performed statistical and graphing analysis using R.",
                    "Promoted to Research Associate II after 15 months for stellar performance and collaboration.",
                ]
            },
            {
                "company": "Bayer Pharmaceuticals",
                "position": "Associate Scientist",
                "date": "Nov. 2016 – Dec. 2017",
                "body": [
                    """Developed an elution buffer formula for a challenging affinity chromatography step in Q1 and Q2
                    that improved product recovery from 10% to 75%.""",
                    """Collaborated with a team of scientists to design and document a scalable downstream process that
                    transitioned from bench scale in Q1 to pilot scale in Q4.""",
                ]
            },
            {
                "company": "University of California, Santa Cruz",
                "position": "Junior Specialist",
                "date": "Mar. 2015 – Aug. 2016",
                "body": [
                    """Conducted experiments that contributed to the discovery of a conserved signaling network that links
                    cell cycle progression to cell membrane growth in S. cerevisiae.""",
                    """Performed densitometry and quantitative analysis on monoclonal and polyclonal western blots to assess
                    phosphorylation states of membrane growth dependent kinases.""",
                ]
            },

        ]
    }
    return render(request, 'frontpage/home.html', context)

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
    paginate_by = 1  # no. posts per page
    
class PostDetailView(DetailView):
    model = Post