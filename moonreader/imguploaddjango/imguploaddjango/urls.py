"""imguploaddjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import Check
from imagehandler.views import ImageUp,text_endpoint
from django.conf import settings
from django.conf.urls.static import static
import requests

urlpatterns = [
    path('admin/', admin.site.urls),
    path('check/', Check.as_view()),
    path('imgup/', ImageUp.as_view()),
    path('img/', ImageUp.as_view()),
    path('text_endpoint/',text_endpoint)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
