from django.conf.urls import url
from management.club import views

urlpatterns = [
    url(r'^$', views.ListClubView.as_view(), name='view'),    
    url(r'^simpan/$', views.SaveClubView.as_view(), name='simpan'),
    # url(r'^edit/(?P<id>\d+)$', views.EditCityRegencyView.as_view(), name='edit'),
    # url(r'^update/$', views.UpdateCityRegencyView.as_view(), name='update'),
    url(r'^hapus/(?P<id>\d+)$', views.HapusClubView.as_view(), name='hapus'),
]