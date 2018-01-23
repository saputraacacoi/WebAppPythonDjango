import os, django

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

INTERNAL_IPS = ('127.0.0.1', '192.168.0.1',)
DEBUG_TOOLBAR_CONFIG = {'INTERCEPT_REDIRECTS': False,}

SECRET_KEY = 'e^r=(#ble-w)ji@_!a3otik+d=ht&#$=$aqwzmhx^on3c$e$ev'
DEBUG = True
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '10.10.1.88',
    'saputra.itec.loc',
]

PROJECT_APPS = [

    'orm',
    'login',
    'management.province',
    'management.cityregency',
    'management.club',
    'library',
    
    'pencab.pgdashboard',
    'penclub.pbdashboard',
    'anggota.adashboard',
]

REQUIRED_APPS = [
    'material',
    'material.frontend',
    'material.admin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'bootstrap4',
    'widget_tweaks',
    'debug_toolbar',
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',  
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
      
]

INSTALLED_APPS = REQUIRED_APPS + PROJECT_APPS

ROOT_URLCONF = 'app.urls'
WSGI_APPLICATION = 'app.wsgi.application'


from app.config.auth import *
from app.config.database import *
from app.config.international import *
from app.config.static import *
django.setup()
from app.config.template import *