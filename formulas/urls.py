from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^subjects/(?P<subject>\w+)/$', views.subjects, name='subject'),
]
