from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page),
    path('urljson', views.urlJson),
    path('textjson', views.textJson),
    
]
