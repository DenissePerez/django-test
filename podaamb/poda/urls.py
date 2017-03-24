from django.conf.urls import url
from . import views

app_name = 'poda'

urlpatterns = [
    # /poda/
    url(r'^$', views.index, name='index'),

    # /poda/id_solicitud
    url(r'^(?P<id_solicitud>[0-9]+)/$', views.detail, name='detail'),
]