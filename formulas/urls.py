from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^formulas/(?P<subject>\w+)/$', views.formulas, name='subject'),
]
