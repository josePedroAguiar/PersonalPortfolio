from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
#from portfolio import views
app_name="cv"
urlpatterns = [
    path('',views.cv,name='cv'),
    path('white',views.wCv,name='wCv'),
]