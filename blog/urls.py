from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
#from portfolio import views
app_name="blog"
urlpatterns = [
    path('',views.all_blogs,name='all_blogs'),
    path('white/',views.all_blogs_w,name='all_blogs_w'),
    path('<int:blog_id>/',views.details,name='details'),
    path('white/<int:blog_id>/',views.details_w,name='details_w')
]