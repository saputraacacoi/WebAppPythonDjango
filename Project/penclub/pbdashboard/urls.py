from django.conf.urls import url
from penclub.pbdashboard import views

urlpatterns = [
    url (r'^view$', views.ListPenClubView.as_view(), name='view'),
    url (r'^detail$', views.DetailClub.as_view(), name='detail'),
    
]
