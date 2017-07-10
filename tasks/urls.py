from django.conf.urls import url
from django.contrib.auth.decorators import login_required, permission_required

from .views import (
    TasksListView,
    TasksDetailView,
)


urlpatterns = [

    url(r'^(?P<pk>[0-9]+)/$', TasksDetailView.as_view(), name='detail'),
    # url(r'^list/$', tasks_list),
    # url(r'^edit/(?P<pk>[0-9]+)/$', auctioneer_detail),
    # url(r'^add/$', auction_list),
    url(r'^$', TasksListView.as_view(), name='list'),

]
