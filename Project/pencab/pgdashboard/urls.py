from django.conf.urls import url
from pencab.pgdashboard import views

urlpatterns = [
    url (r'^view$', views.ListPencabView.as_view(), name='view'),
]
