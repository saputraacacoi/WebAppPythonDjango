from django.conf.urls import url
from login import views


urlpatterns =[
    url(r'^$', views.LoginView.as_view(), name='view'),
    url(r'^doLogin$', views.DoLoginView.as_view(), name='doLogin'),
    url(r'^doLogout$', views.DoLogoutView.as_view(), name='doLogout'),
]