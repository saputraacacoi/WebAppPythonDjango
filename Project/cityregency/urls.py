from django.conf.urls import url
from cityregency import views

urlpatterns = [
    url(r'^/$', views.ListCityRegencyView.as_view(), name='view'),    
    url(r'^tambah/$', views.AddCityRegencyView.as_view(), name='tambah'),
    url(r'^simpan/$', views.SaveCityRegencyView.as_view(), name='simpan'),
    url(r'^edit/(?P<id>\d+)$', views.EditCityRegencyView.as_view(), name='edit'),
    url(r'^update/$', views.UpdateCityRegencyView.as_view(), name='update'),
    url(r'^hapus/(?P<id>\d+)$', views.HapusCityRegencyView.as_view(), name='hapus'),
]