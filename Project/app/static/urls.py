"""WebApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from app.config import setting
import debug_toolbar

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^__debug__/', include(debug_toolbar.urls)),
    
    url(r'^province/', include('management.province.urls', namespace='province')),
    url(r'^cityregency/', include('management.cityregency.urls', namespace='cityregency')),
    url(r'^pgdashboard/', include('pencab.pgdashboard.urls', namespace='pgdashboard')),
    url(r'^pbdashboard/', include('penclub.pbdashboard.urls', namespace='pbdashboard')),
    url(r'^club/', include('management.club.urls', namespace='club')),
    url(r'^', include('login.urls', namespace='login')),
]

urlpatterns +=  staticfiles_urlpatterns()

