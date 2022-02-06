from django.shortcuts import render
from .models import Project

def home(request):
    projects=Project.objects.all()
    return render(request, "portfolio/index.html",{'projects':projects})
def wHome(request):
    projects=Project.objects.all()
    return render(request, "portfolio/white/index.html",{'projects':projects})