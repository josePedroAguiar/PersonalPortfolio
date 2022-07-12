from django.shortcuts import render
from .models import Project
import datetime

def home(request):
    projects=Project.objects.all()
    x=datetime.datetime.now()
    old= (int)(x.strftime("%y"))-1;
    return render(request, "portfolio/index.html",{'projects':projects,"date":old})
def wHome(request):
    projects=Project.objects.all()
    x=datetime.datetime.now()
    old= (int)(x.strftime("%y"))-1;
    return render(request, "portfolio/white/index.html",{'projects':projects,"date":old})