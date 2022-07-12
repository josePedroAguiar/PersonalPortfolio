from django.shortcuts import render
from .models import Skill,Language,Education,Work

def cv(request):
    skills=Skill.objects.all()
    languages=Language.objects.all()
    educations=Education.objects.all()
    works=Work.objects.all()
    data={"work":"Software engineer","email":"jpaguiar@gmail.com", "name":"José Pedro Aguiar","phone":"927396759","local":"Viseu,PT"}
    return render(request, "cv/cv.html" ,{'works':works,'languages':languages,'educations':educations,'skills':skills,"data":data})
# Create your views here.
def wCv(request):
    skills=Skill.objects.all()
    languages=Language.objects.all()
    educations=Education.objects.all()
    works=Work.objects.all()
    data={ "work":"Software engineer","email":"jpaguiar@gmail.com", "name":"José Pedro Silva Aguiar","phone":"927396759","local":"Viseu,PT"}
    return render(request, "cv/white/cv.html" ,{'works':works,'languages':languages,'educations':educations,'skills':skills,"data":data})