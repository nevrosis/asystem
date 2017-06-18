"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from auctions.views import (
    auction_detail,
    item_list,
    item_detail,
    auction_list,
    auctioneer_detail,
    auctioneer_list,
    item_listing,
    auction_listing
)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/auctioneers/$', auctioneer_list),
    url(r'^api/auctioneers/(?P<pk>[0-9]+)/$', auctioneer_detail),
    url(r'^api/auctions/$', auction_list),
    url(r'^api/auctions/(?P<pk>[0-9]+)/$', auction_detail),

    url(r'^api/auction_listing/(?P<auction_id>[0-9]+)/$', auction_listing),
    url(r'^api/item_listing/(?P<auction_id>[0-9]+)/$', item_listing),

    url(r'^api/items/$', item_list),
    url(r'^api/items/(?P<pk>[0-9]+)/$', item_detail),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
