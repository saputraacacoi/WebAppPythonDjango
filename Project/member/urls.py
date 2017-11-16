from django.conf.urls import url
from member import views

urlpatterns = [
    url (r'^test$', views.TestView.as_view(), name='test'),
    url (r'^cobatemplate$', views.Tsttemplate.as_view(), name='tpl'),
]