from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # url(r'^$', include('register.urls')),
    url(r'^user/', include('register.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^twister/', include('twister.urls')),
]
