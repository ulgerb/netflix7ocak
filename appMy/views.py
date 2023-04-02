from django.shortcuts import render
from appUser.models import Profile

# Create your views here.

def index(request):
    context = {}
    return render(request,'index.html', context)

def indexBrowse(request, slug):
    profil = Profile.objects.filter(user = request.user).get(slug=slug)
    
    context = {
        "profil": profil,
    }
    return render(request,'browse-index.html', context)
