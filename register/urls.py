from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

app_name = 'register'
urlpatterns = [
    url(r'^logout/$', auth_views.logout, {'template_name': 'register/login.html'}, name='logout'),
    url(r'^$', auth_views.login, {'template_name': 'register/login.html'}, name='login'),
    url(r'^register/$', views.Registration.as_view(), name='registration'),
]
