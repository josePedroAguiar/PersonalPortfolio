from django.shortcuts import render
from .models import Skill,Language,Education,Work

def cv(request):
    skills=Skill.objects.all()
    languages=Language.objects.all()
    educations=Education.objects.all()
    works=Work.objects.all()
    return render(request, "cv/cv.html" ,{'works':works,'languages':languages,'educations':educations,'skills':skills})
# Create your views here.
def wCv(request):
    skills=Skill.objects.all()
    languages=Language.objects.all()
    educations=Education.objects.all()
    works=Work.objects.all()
    return render(request, "cv/white/cv.html" ,{'works':works,'languages':languages,'educations':educations,'skills':skills})