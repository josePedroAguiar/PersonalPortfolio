from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=240)
    description=models.TextField()
    date= models.DateTimeField(null=False)
    #image=models.ImageField(blank=True,upload_to='cv/images/')
    #url=models.URLField(blank=True)

    def __str__(self):
        return self.title