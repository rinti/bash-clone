from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^vote/(?P<pk>\d+)/$', views.vote),
    url(r'^top/$', views.TopView.as_view(), name='top'),
    url(r'^$', views.HomeView.as_view(), name='home'),
]
