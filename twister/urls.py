from django.conf.urls import url

from . import views

app_name = 'twister'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^twist/$', views.TwistView.as_view(), name='twist'),
    url(r'^domain/(?P<pk>.+)/$', views.DomainView.as_view(), name='domain'),
]
