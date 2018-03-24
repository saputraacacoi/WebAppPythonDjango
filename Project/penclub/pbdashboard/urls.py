from django.conf.urls import url
from penclub.pbdashboard import views

urlpatterns = [
    url (r'^view$', views.DetailClubView.as_view(), name='view'),
    url (r'^edit$', views.UbahClubView.as_view(), name='edit'),
    url (r'^club/update$', views.UpdateClubView.as_view(), name='update'),
    url (r'^club/documents$', views.BerkasView.as_view(), name='documents'),
    url (r'^club/documents/upload$', views.BerkasUploadView.as_view(), name='d_upload'),
    url (r'^delete/(?P<pk>\d+)$', views.HapusBerkasView.as_view(), name='delete'),

    #anggota
    url (r'^anggota$', views.ListAnggotaView.as_view(), name='anggota'),
    url (r'^detail_anggota/(?P<pk>\d+)$', views.DetailAnggotaView.as_view(), name='detail_anggota'),
    url (r'^add_anggota$', views.AddAnggotaView.as_view(), name='add_anggota'),
    url (r'^save_anggota$', views.SaveAnggotaView.as_view(), name='save_anggota'),
    url(r'^hapus_anggota/(?P<id>\d+)$', views.HapusAnggotaView.as_view(), name='hapus_anggota'),
]
