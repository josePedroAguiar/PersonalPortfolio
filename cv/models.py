from django.db import models
class Skill(models.Model):
    name=models.CharField(max_length=120)
    perc=models.CharField(max_length=4)
    #date= models.DateTimeField(null=False)
    #image=models.ImageField(blank=True,upload_to='cv/images/')
    #url=models.URLField(blank=True)

    def __str__(self):
        return self.name
class Language(models.Model):
    name=models.CharField(max_length=120)
    perc=models.CharField(max_length=4)

    def __str__(self):
        return self.name
# Create your models here.
class Work(models.Model):
    title=models.CharField(max_length=240)
    description=models.CharField(max_length=1000)
    dateS= models.DateTimeField(null=False)
    dateE= models.DateTimeField(null=False)

    def __str__(self):
        return self.title

class Education(models.Model):
    title=models.CharField(max_length=240)
    description=models.CharField(max_length=1000)
    dateS= models.DateTimeField(null=False)
    dateE= models.DateTimeField(null=False)

    def __str__(self):
        return self.title
# Create your models here.
