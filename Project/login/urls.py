from django.conf.urls import url
from login import views

urlpatterns = [
    url(r'^view$', views.LoginView.as_view(), name='view'),
]   