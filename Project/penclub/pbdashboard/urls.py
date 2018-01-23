from django.conf.urls import url
from penclub.pbdashboard import views

urlpatterns = [
    url (r'^view$', views.ListPenClubView.as_view(), name='view'),
    url (r'^detail$', views.DetailClub.as_view(), name='detail'),
    url (r'^edit$', views.UbahClub.as_view(), name='edit'),
    url (r'^club/update$', views.UpdateView.as_view(), name='update'),
    url (r'^club/documents$', views.BerkasView.as_view(), name='documents'),
    url (r'^club/documents/upload$', views.BerkasUploadView.as_view(), name='d_upload'),
    url(r'^delete/(?P<pk>\d+)$', views.HapusBerkasView.as_view(), name='delete'),
]
