from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

app_name = 'register'
urlpatterns = [
    url(r'^login/$', auth_views.login, {'template_name': 'register/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'register/index.html'}, name='logout'),
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^register/$', views.Registration.as_view(), name='registration'),
    # url(r'^login/$', views.Login.as_view(), name='login'),
]
