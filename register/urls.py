from django.conf.urls import url

from . import views

app_name = 'register'
urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^register/$', views.Registration.as_view(), name='registration'),
    url(r'^login/$', views.Login.as_view(), name='login'),
]
