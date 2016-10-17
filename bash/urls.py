from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^vote/(?P<pk>\d+)/$', views.vote),
    url(r'^$', views.HomeView.as_view()),
]
