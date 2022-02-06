from django.shortcuts import render,get_object_or_404
from .models import Blog
# Create your views here.
def all_blogs(request):
    blogs_count=Blog.objects.count()
    blogs=Blog.objects.all()
    return render(request, "blog/index.html",{'blogs':blogs,'blogs_count':blogs_count})
def all_blogs_w(request):
    blogs_count=Blog.objects.count()
    blogs=Blog.objects.all()
    return render(request, "blog//white/index.html",{'blogs':blogs,'blogs_count':blogs_count})
def details_w(request,blog_id):
    blog=get_object_or_404(Blog,pk=blog_id)
    return render(request, "blog/white/blog.html",{'blog':blog})
def details(request,blog_id):
    blog=get_object_or_404(Blog,pk=blog_id)
    return render(request, "blog/blog.html",{'blog':blog})
