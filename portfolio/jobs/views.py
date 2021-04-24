from django.shortcuts import render
from .models import Job

# Create your views here.
def home(request):
    jobs=Job.objects.all
    return render(request, "jobs/home.html", {"jobs":jobs})

def showcase(request):
    return render(request, "showcase/index.html")

def wordcount(request):
    return render(request, "wordcount/index.html")