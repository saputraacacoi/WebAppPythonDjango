from django.conf.urls import url
from province import views

urlpatterns = [
    url (r'^$', views.ListProvinceView.as_view(), name='view'),
    url(r'^tambah/$', views.AddProvinceView.as_view(), name='tambah'),
    url(r'^simpan/$', views.SaveProvinceView.as_view(), name='simpan'),
    url(r'^edit/(?P<id>\d+)$', views.EditProvinceView.as_view(), name='edit'),
    url(r'^update/$', views.UpdateProvinceView.as_view(), name='update'),
    url(r'^hapus/(?P<id>\d+)$', views.HapusProvinceView.as_view(), name='hapus'),
]