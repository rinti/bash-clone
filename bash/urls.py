from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^vote/(?P<pk>\d+)/$', views.vote),
    url(r'^user/(?P<pk>\d+)/$', views.UserListView.as_view(), name='user'),
    url(r'^top/$', views.TopListView.as_view(), name='top'),
    url(r'^$', views.HomeView.as_view(), name='home'),
]
